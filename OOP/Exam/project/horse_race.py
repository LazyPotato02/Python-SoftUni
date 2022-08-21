class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = list()

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        self._validate_seasons(value)
        self.__race_type = value

    @staticmethod
    def _validate_seasons(value):
        seasons = ["Winter", "Spring", "Autumn", "Summer"]
        if value not in seasons:
            raise ValueError("Race type does not exist!")
