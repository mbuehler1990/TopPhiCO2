

class UseCase:

    """

    Class holding zone use case;

    ID: ID of the zone source profile
        Integer 1x1

    Name: Name of use case
        string
    Persons: Number of people in the room
        Integer 1x1 or array [Time,People]
    CO2_Source: CO2 Emission rate into Zone [l/h]
        Integer 1x1 or array [Time,CO2_Source]
    CO2_Source_pP: CO2 Emission rate into Zone per person [l/h]
        Integer 1x1

    VapMoisture_Source: vaporous moisture Emission rate into Zone [kg/h]
        Integer 1x1 or array [Time,VapMoisture_Source]
    VapMoisture_Source_pP: vaporous moisture Emission rate into Zone per person [kg/h Person]
        Integer 1x1

    KonvHeat_Source: konvective heat source [W]
        Integer 1x1 or array [Time,KonvHeat_Source]
    KonvHeat_Source_pP: konvective heat source per person [W]
        Integer 1x1

    RadHeat_Source: radiative heat source [W]
        Integer 1x1 or array [Time,RadHeat_Source]
    RadHeat_Source_pP: radiative heat source per person [W]
        Integer 1x1

    OpenWindow: control parameter to open all Windows of the zone
        int 1x1 [0...1]

    """

    numOfInstances = 0

    def newInstances(cls):
        cls.numOfInstances += 1

    newInstances = classmethod(newInstances)

    def getNumInstances(cls):
        return cls.numOfInstances

    getNumInstances = classmethod(getNumInstances)

    def __init__(self, dict):
        self.newInstances()

        # init with default values
        self.ID = self.numOfInstances
        self.Name = []
        self.Persons = 0
        self.CO2_Source = 0
        self.CO2_Source_pP = 20
        self.VapMoisture_Source = 0
        self.VapMoisture_Source_pP = 0.035
        self.KonvHeat_Source = 0
        self.KonvHeat_Source_pP = 60
        self.RadHeat_Source = 0
        self.RadHeat_Source_pP = 60
        self.OpenWindow = 0

        # Overwrite default values with received entries
        for key in dict:
            setattr(self, key, dict[key])
















