
import numpy as np
from Functions import getRowCol

from OCC.Display.SimpleGui import init_display
from OCC.BRepBuilderAPI import BRepBuilderAPI_Sewing
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeSolid
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeShell

from OCC.BRepClass3d import BRepClass3d_SolidClassifier

from OCC.BRepGProp import brepgprop
from OCC.GProp import GProp_GProps
from OCC.BRepAlgoAPI import *
from OCC.TopoDS import topods

from OCC.ShapeFix import ShapeFix_Shell


from OCCUtils import Construct


class Zone:
    """

    Class holding zone properties;

    ________________________________
    Zone geometrical properties
    ________________________________

    Vol: Volume [m³]
        Integer 1x1
    FloorArea: Floor Area of the Zone [m²]
        Integer 1x1
    FloorAreaID: ID of floor Area patch(es)
        integer array [nx1]
    Surfaces: ID of Surfaces containing to zone
        integer array [nx1]

    ________________________________
    Zone Air properties
    ________________________________

    X: Absolute Humidity [kg/kg]
        Integer 1x1
        -> controlled Variable
    R: Relative Humidity [-]
        Integer 1x1 in range [0...1]
        -> controlled Variable
    CO2-Conc: CO2 concentration [ppm]
        Integer 1x1
        -> controlled Variable
    T_Air: air temperature [K]
        Integer 1x1
        -> controlled Variable
    T_op: operative temperature [K]
        Integer 1x1
        -> controlled Variable
    P: humid air pressure [Pa]
        Integer 1x1
    Pv: vapour partial pressure [Pa]
        Integer 1x1
    Pda: dry air partial pressure [Pa]
        Integer 1x1
    Rho: humid air density [kg/m³]
        Integer 1x1
    H: humid air enthalpie [J/kg]
        Integer 1x1


    ________________________________
    Natural Infiltration
    ________________________________

    NI_n: air change rate for natural infiltration [1/h]
        Integer 1x1 or array [Time,NI_n]
    NI_Vdot: volume flow of infiltrated air [m³/s]
        Integer 1x1 or array [Time,NI_Vdot]
    NI_Mdot: mass flow of infiltrated air [kg/s]
        Integer 1x1 or array [Time,NI_Mdot]
    NI_T: temperature of infiltrated air [K]
        Integer 1x1 or array [Time,NI_T]
    NI_R: relative humidity of infiltrated air [-]
        Integer 1x1 or array [Time,NI_R]
    NI_X: absolute humidity of infiltrated air [kg/kg]
        Integer 1x1 or array [Time,NI_X]
    NI_Rho: Density of infiltrated air [kg/m³]
        Integer 1x1 or array [Time,NI_Rho]

    ________________________________
    Mechanical infiltration
    ________________________________

    MI_n: air change rate for mechanical infiltration [1/h]
        Integer 1x1 or array [Time,MI_n]
    MI_Vdot: volume flow of mechanical infiltrated air [m³/s]
        Integer 1x1 or array [Time,MI_Vdot]
    MI_Mdot: mass flow of mechanical infiltrated air [kg/s]
        Integer 1x1 or array [Time,MI_Mdot]
    MI_T: temperature of mechanical infiltrated air [K]
        Integer 1x1 or array [Time,MI_T]
    MI_R: relative humidity of mechanical infiltrated air [-]
        Integer 1x1 or array [Time,MI_R]
    MI_X: absolute humidity of mechanical infiltrated air [kg/kg]
        Integer 1x1 or array [Time,MI_X]
    MI_Rho: Density of mechanical infiltrated air [kg/m³]
        Integer 1x1 or array [Time,MI_Rho]

    ________________________________
    Zone UseCase
    ________________________________

    UseCaseID: ID of the zone source profile
        Integer 1x1
    CO2_Source: CO2 Emission rate into Zone [l/h]
        Integer 1x1 or array [Time,CO2_Source]
    VapMoisture_Source: vaporous moisture Emission rate into Zone [kg/h]
        Integer 1x1 or array [Time,VapMoisture_Source]
    LiqMoisture_Source: liquid moisture Emission rate into Zone [kg/h]
        Integer 1x1 or array [Time,LiqMoisture_Source]
    KonvHeat_Source: konvective heat source [W]
        Integer 1x1 or array [Time,KonvHeat_Source]
    RadHeat_Source: radiative heat source [W]
        Integer 1x1 or array [Time,RadHeat_Source]


    """

    def __init__(self, dict):
        # init with default values
        #________________________________
        # Zone geometrical properties
        #________________________________

        self.Vol = []
        self.FloorArea = []
        self.FloorAreaID = []
        self.Surfaces = []
        self.X = 0
        self.R = 0
        self.CO2_Conc = 0
        self.T_Air = 293.15
        self.T_op = 293.15
        self.P = 101300
        self.Pv = 0
        self.Pda = 101300
        self.Rho = 1.2049
        self.H = 293556.945

        #________________________________
        # Natural Infiltration
        #________________________________

        self.NI_n = 0.08
        self.NI_Vdot = 0
        self.NI_Mdot = 0
        # self.NI_T = []
        # self.NI_R = []
        # self.NI_X = []
        # self.NI_Rho = []

        #________________________________
        # Mechanical infiltration
        #________________________________

        self.MI_n = 0.5
        self.MI_Vdot = []
        self.MI_Mdot = []
        self.MI_T = []
        self.MI_R = []
        self.MI_X = []
        self.MI_Rho = []

        # ________________________________
        # Zone UseCase
        #________________________________

        self.UseCaseID = 1

        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])

    def UpdateZone(self, Surfaces, display):
        print(self.Surfaces)

        sewing = BRepBuilderAPI_Sewing()
        for i in self.Surfaces:
            sewing.Add(Surfaces[i].GHShape)
        sewing.Perform()
        sewed_shape = sewing.SewedShape()

        tds = topods()

#        FixedShape = ShapeFix_Shell(tds.Shell(sewed_shape))
#        FixedShape.Perform()

        solid = BRepBuilderAPI_MakeSolid(tds.Shell(sewed_shape))

#        Test = BRepClass3d_SolidClassifier() 
#        Test.Perform()



        display.DisplayShape(solid.Shape())

        #print('done')

        Props = GProp_GProps()
        brepgprop.VolumeProperties(solid.Shape(), Props)
        self.Vol = Props.Mass()

        print(self.Vol)

        return display









