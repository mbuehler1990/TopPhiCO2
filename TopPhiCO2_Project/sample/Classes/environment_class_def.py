

class Environment:
    """

    Class holding environmental properties;

    Air_T: Temperature [K]:
        Can be double or array with [Time, T]
    Air_R: Relative Humidity 0...1 [-]:
        Can be double or array with [Time, R]
    V_N: Wind speed in north direction [m/s]:
        Can be double or array with [Time, V_N]
    V_E: Wind speed in east direction [m/s]:
        Can be double or array with [Time, V_E]
    SolIrr_Dir: Direct irradiation from sun on horizontal plane [W/m²]:
        Can be double or array with [Time, SolIrr_Dir]
    SolIrr_Diff: Diffuse irradiation from sun on horizontal plane [W/m²]:
        Can be double or array with [Time, SolIrr_Diff]
    SkyCov: cloud covered part of the sky 0...1 [-]
        Can be double or array with [Time, SkyCov]
    Precip: Precipitation [mm/h]
        Can be double or array with [Time, Precipitation]

    """

    def __init__(self, dict):
        # init with default values
        self.T = 293.15
        self.R = 0.5
        self.V_N = 2
        self.V_E = 0
        self.SollIrr_Dir = 0
        self.SolIrr_Diff = 0
        self.SkyCov = 0
        self.Precip = 0
        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])
















