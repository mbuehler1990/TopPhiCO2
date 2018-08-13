

from OCC.gp import *


class Point:
    """

    Class holding point  properties;

    X: x Koordinate [m]
    Y: y Koordinate [m]
    Z: z Koordinate [m]

    """

    def createPointObj(self):
        self.Point = gp_Pnt(self.X, self.Y, self.Z)

    def __init__(self, dict):
        # init with default values
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.Point = []
        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])
            self.createPointObj()



















