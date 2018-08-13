
import numpy as np
from Functions import getRowCol

from OCC.Display.SimpleGui import init_display
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakePolygon
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeShape
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeFace

from OCC.BRepGProp import BRepGProp_Face
from OCC.BRepGProp import brepgprop
from OCC.GProp import GProp_GProps
from OCC.BRepAlgoAPI import *

from OCC.TopoDS import TopoDS_Shape
from OCC.TopOpeBRep import TopOpeBRep_ShapeIntersector



class Surf:

    """

    Class holding surface properties;

    ID: ID of the surface [-]:
        int 1x1
    PolygonPoints
        array [nx1]
    Geometry: surface object
        tbd
    Normal: surface normal
        array [3x1]
    Area: surface area [m²]
        double 1x1
    Opening: opening polygons
        array [n x n]
    PartID: ID of the part to assign
        int 1x1

    Surface Definition:

                |      |
                |      |
    Side 1      |      |    Side 2
                |      |
            ------------------>   Surface normal
                |      |
                |      |
                |      |

     ------------------------------
     Side 1
     ------------------------------

    Side1_Zone: adjacent Zone ID of side 1 (surface normal origin)
        int 1x1

    Side1_Adj: adjacent area
        0: Auto (automatic allocation)
        1: Zone
        2: Outside Air
        3: Soil
        4: User specified

    Side1_HeatFlow: heat flow over side 1 surface; only applied if Side1Adj == 3
        int 1x1 or array [Time,Side1HeatFlow]
        Unit: [W]

    Side1_T: surface temperature
        int 1x1 or array [Time,Side1_T]
        Unit: [K]

    Side1_RelHum: adjacent relative humidity to side 1
        int 1x1 or array [Time,Side1_RelHum]
        Unit: [-]

    Side1_TAir: adjacent air temperature
        int 1x1 or array [Time,Side1_TAir]
        Unit: [K]

    Side1_TAir: adjacent air temperature
        int 1x1 or array [Time,Side1_TAir]
        Unit: [K]



     ------------------------------
     Side 2
     ------------------------------


    Side2_Zone: adjacent Zone ID of side 2 (surface normal origin)
        int 1x1

    Side2_Adj: adjacent area
        0: Auto (automatic allocation)
        1: Zone
        2: Outside Air
        3: Soil
        4: User specified

    Side2_HeatFlow: heat flow over side 2 surface; only applied if Side1Adj == 3
        int 1x1 or array [Time,Side1HeatFlow]
        Unit: [W]

    Side2_T: surface temperature
        int 1x1 or array [Time,Side1_T]
        Unit: [K]

    Side2_RelHum: adjacent relative humidity to side 2
        int 1x1 or array [Time,Side1_RelHum]
        Unit: [-]

    Side2_TAir: adjacent air temperature
        int 1x1 or array [Time,Side1_TAir]
        Unit: [K]

    Side2_TAir: adjacent air temperature
        int 1x1 or array [Time,Side1_TAir]
        Unit: [K]


    """

    def __init__(self, dict):
        # init with default values

        self.ID = []
        self.PolygonPoints = np.array([])
        self.Geometry = []
        self.Normal = []
        self.Area = []
        self.Opening = []
        self.PartID = []

        # ------------------------------
        # Side 1
        # ------------------------------

        self.Side1_Zone = []
        self.Side1_Adj = []
        self.Side1_HeatFlow = []
        self.Side1_T = []
        self.Side1_RelHum = []
        self.Side1_TAir = []

        # -----------------------------
        # Side 2
        # ------------------------------

        self.Side2_Zone = []
        self.Side2_Adj = []
        self.Side2_HeatFlow = []
        self.Side2_T = []
        self.Side2_RelHum = []
        self.Side2_TAir = []

        # ------------------------------
        # Graphic objects
        # ------------------------------

        self.GHPolygon = []
        self.GHFace = []
        self.GHShape = []

        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])

    def createGraphicObjects(self, points, display):

        self.GHPolygon = BRepBuilderAPI_MakePolygon()

        for i in self.PolygonPoints:
            if i in range(len(points)):
                self.GHPolygon.Add(points[i].Point)
            else:
                print('polygon point %d does not exist' % i)

        self.GHPolygon.Close()
        self.GHFace = BRepBuilderAPI_MakeFace(self.GHPolygon.Wire())
        self.GHShape = BRepBuilderAPI_MakeShape.Shape(self.GHFace)

        #display.DisplayShape(self.GHShape)

        if len(self.Opening) > 0:
            print('processing openings')
            for i in range(len(self.Opening)):
                openingpolygon = BRepBuilderAPI_MakePolygon()
                for j in self.Opening[i]:
                    openingpolygon.Add(points[j].Point)
                openingpolygon.Close()
                openingface = BRepBuilderAPI_MakeFace(openingpolygon.Wire())
                openingshape = BRepBuilderAPI_MakeShape.Shape(openingface)
                Cut = BRepAlgoAPI_Cut(self.GHShape, openingshape)
                self.GHShape = Cut.Shape()

        #display.DisplayShape(self.GHShape)

        # calculate Area
        Props = GProp_GProps()
        brepgprop.SurfaceProperties(self.GHShape, Props)
        self.Area = Props.Mass()

        return display

    def update(self, dict):
        for key in dict:
            setattr(self, key, dict[key])

    def updateGraphicObjects(self, points, display):

        self.GHPolygon = []

        for i in self.PolygonPoints:
            if i in range(len(points)):
                self.GHPolygon.Add(points[i].Point)
            else:
                print('polygon point %d does not exist' % i)

        self.GHPolygon.Close()
        self.GHFace = BRepBuilderAPI_MakeFace(self.GHPolygon.Wire())
        self.GHShape = BRepBuilderAPI_MakeShape.Shape(self.GHFace)

        #display.DisplayShape(self.GHShape)

        if len(self.Opening) > 0:
            print('processing openings')
            for i in range(len(self.Opening)):
                openingpolygon = BRepBuilderAPI_MakePolygon()
                for j in self.Opening[i]:
                    openingpolygon.Add(points[j].Point)
                openingpolygon.Close()
                openingface = BRepBuilderAPI_MakeFace(openingpolygon.Wire())
                openingshape = BRepBuilderAPI_MakeShape.Shape(openingface)
                cut = BRepAlgoAPI_Cut(self.GHShape, openingshape)
                self.GHShape = cut.Shape()

        #display.DisplayShape(self.GHShape)

        # calculate Area
        Props = GProp_GProps()
        brepgprop.SurfaceProperties(self.GHShape, Props)
        self.Area = Props.Mass()














