


from tkinter import Tk
from tkinter.filedialog import askopenfilename


from Classes import environment_class_def
from Classes import soil_class_def
from Classes import zone_class_def
from Classes import usecase_class_def
from Classes import surf_class_def
from Classes import building_class_def
from Classes import point_class_def
# from Functions import import_stl




import numpy as np

from OCC.Display.SimpleGui import init_display

from OCC.Display.OCCViewer import Display3d

from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakePolygon
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeShape
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeFace


def main():
    """Entry point for the application script"""
    print("Call your main application code here")


T = np.array([[99999991, 283],
              [99999992, 284],
              [99999992, 284]])

UseCases = []
Locations = []
Soils = []
Zones = []
Surfaces = []
Buildings = []
Environments = []
Points = []


Locations.append(environment_class_def.Environment({'T': T}))
Soils.append(soil_class_def.Soil({}))



Buildings.append(building_class_def.Building({}))


UseCases.append(usecase_class_def.UseCase({}))
UseCases.append(usecase_class_def.UseCase({}))
UseCases.append(usecase_class_def.UseCase({}))


# define new point:

# 0
Points.append(point_class_def.Point({'X': 0, 'Y': 0, 'Z': 0}))
# 1
Points.append(point_class_def.Point({'X': 3, 'Y': 0, 'Z': 0}))
# 2
Points.append(point_class_def.Point({'X': 3, 'Y': 2, 'Z': 0}))
# 3
Points.append(point_class_def.Point({'X': 0, 'Y': 2, 'Z': 0}))
# 4
Points.append(point_class_def.Point({'X': 0, 'Y': 0, 'Z': 10}))
# 5
Points.append(point_class_def.Point({'X': 3, 'Y': 0, 'Z': 10}))
# 6
Points.append(point_class_def.Point({'X': 3, 'Y': 2, 'Z': 10}))
# 7
Points.append(point_class_def.Point({'X': 0, 'Y': 2, 'Z': 10}))

# window 1 points
# 8
Points.append(point_class_def.Point({'X': 0.1, 'Y': 0, 'Z': 0.25}))
# 9
Points.append(point_class_def.Point({'X': 0.4, 'Y': 0, 'Z': 0.25}))
# 10
Points.append(point_class_def.Point({'X': 0.1, 'Y': 0, 'Z': 0.75}))
# 11
Points.append(point_class_def.Point({'X': 0.4, 'Y': 0, 'Z': 0.75}))




# window 2 points
# 12
Points.append(point_class_def.Point({'X': 0.6, 'Y': 0, 'Z': 0.25}))
# 13
Points.append(point_class_def.Point({'X': 0.9, 'Y': 0, 'Z': 0.25}))
# 14
Points.append(point_class_def.Point({'X': 0.6, 'Y': 0, 'Z': 0.75}))
# 15
Points.append(point_class_def.Point({'X': 0.9, 'Y': 0, 'Z': 0.75}))


display, start_display, add_menu, add_function_to_menu = init_display()

# 0
PolygonPoints = []
PolygonPoints.append(np.array([0, 1, 2, 3]))
PolygonPoints.append(np.array([1, 2, 6, 5]))
PolygonPoints.append(np.array([2, 3, 7, 6]))
PolygonPoints.append(np.array([5, 6, 7, 4]))
PolygonPoints.append(np.array([0, 4, 7, 3]))
PolygonPoints.append(np.array([0, 1, 5, 4]))

PolygonPoints.append(np.array([8, 9, 11, 10]))
PolygonPoints.append(np.array([12, 13, 15, 14]))

# 0
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[0]}))
# 1
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[1]}))
# 2
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[2]}))
# 3
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[3]}))
# 4
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[4]}))
# 5
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[5], 'Opening': [PolygonPoints[6], PolygonPoints[7]]}))
# 6
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[6]}))
# 7
Surfaces.append(surf_class_def.Surf({'PolygonPoints': PolygonPoints[7]}))




# import geometry from stl file

# tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#
# import_stl(filename, Points, PolygonPoints, Surfaces)


# Create new zone:

ZoneSurfaces = []
ZoneSurfaces.append(np.array([0, 1, 2, 3, 4, 5, 6, 7]))

Zones.append(zone_class_def.Zone({'Surfaces': ZoneSurfaces[0]}))



for i in range(len(Surfaces)):
    display = Surfaces[i].createGraphicObjects(Points, display)


for i in range(len(Zones)):
    display = Zones[i].UpdateZone(Surfaces, display)



#i = 5
#Surfaces[i] = surf_class_def.Surf({'PolygonPoints': PolygonPoints[5]})
#display = Surfaces[i].createGraphicObjects(Points, display)

print('done')


# GHPoint = BRepBuilderAPI_MakeVertex(Points[0].Point)
# Shape = BRepBuilderAPI_MakeShape.Shape(GHPolygon)
# display.DisplayShape(Shape2)




def simple_test(event=None):
    display.Test()





def simple_cylinder(event=None):
    from OCC.BRepPrimAPI import BRepPrimAPI_MakeCylinder
    s = BRepPrimAPI_MakeCylinder(60, 200).Shape()
    display.DisplayShape(s)


add_menu('simple test')
add_function_to_menu('simple test', simple_test)
add_function_to_menu('simple test', simple_cylinder)

display.View_Iso()
display.FitAll()
# display loop
start_display()

