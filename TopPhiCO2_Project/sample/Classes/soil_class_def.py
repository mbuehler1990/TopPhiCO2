class Soil:
    """

    Class holding soil properties;

    T: Soil Temperature [K]
        Can be double or array with [Time, Soil_T] or [Time, Depth, Soil_T]
    D: Soil Layer thickness [m]
        Can be double or array with [Soil_D]
    Lambda: Soil Layer lambda [W/m]
        Can be double or array with [Soil_Lambda] or array with [Soil_Lambda,]
    Rho: Soil Layer density [kg/m³]
        Can be double or array with [Soil_Rho]
    Cp: Soil Layer specific heat capacity at constant pressure [J/kgK]
        Can be double or array with [Soil_Cp]
    Cp: Soil temperature in huge distance (100m) [K]
        double

    """

    def __init__(self, dict):
        # set default values
        self.T = 283.15
        self.D = 1
        self.Lambda = 1.84
        self.Rho = 2040
        self.Cp = 0.52
        self.T_inf = 283.15
        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])