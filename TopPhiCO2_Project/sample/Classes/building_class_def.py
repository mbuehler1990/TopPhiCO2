

class Building:
    """

    Class holding building  properties;

    Zones: zones ID
        integer array
    HR: ventilation system with heat recovery
        [0] or [1]
    HR_EE: HeatRecovery_EnthalpieEfficiency:
        [0...1]
    HR_RWE: HeatRecovery_RewettingEfficiency:
        [0...1]
    ...

    """

    def __init__(self, dict):
        # init with default values
        self.Zones = []
        self.HR = 0
        self.HR_EE = 0
        self.HR_RWE = 0
        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])
















