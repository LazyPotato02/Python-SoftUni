from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = list()
        self.jockeys = list()
        self.horse_races = list()

    # ---------------------------METHODS--------------------------------------#

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.__initialize_horse(horse_type, horse_name, horse_speed)
        self.__validate_horse(horse)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        self.__validate_jockey(jockey)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = HorseRace(race_type)
        self.__validate_race(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey(jockey_name)
        res = self.__check_jockey_horse(jockey)
        if res:
            return f"Jockey {jockey_name} already has a horse."
        horse = self.__find_horse_of_type(horse_type)
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._find_race(race_type)
        jockey = self.__find_jockey(jockey_name)
        self.__validate_jockey_has_horse(jockey)
        val_jock_in_race = self._validate_jockey_not_in_race(jockey, race)
        if val_jock_in_race is True:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_race(race_type)
        race_found = self.__validate_horse_race(race_type)
        if not race_found:
            raise Exception(f"Race {race_type} could not be found!")
        self.__validate_participants_in_race(race)
        winner, max_speed = self.__race_horses(race)
        return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    # ---------------------------HELPERS--------------------------------------#

    def __validate_horse(self, horse):
        if horse in self.horses:
            raise Exception(f"Horse {horse.name} has been already added!")

    def __validate_jockey(self, jockey):
        if jockey in self.jockeys:
            raise Exception(f"Jockey {jockey.name} has been already added!")

    def __validate_race(self, race_type):
        for race in self.horse_races:
            if race_type == race.race_type:
                raise Exception(f"Race {race_type} has been already created!")

    def __find_horse_of_type(self, horse_type):
        for horse in reversed(self.horses):
            if horse.TYPE == horse_type:
                self.horses.remove(horse)
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

        raise Exception(f"Jockey {jockey_name} could not be found!")

    def _find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f"Race {race_type} could not be found!")

    def __validate_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return True
        return False

    @staticmethod
    def __validate_jockey_has_horse(jockey):
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

    @staticmethod
    def __initialize_horse(horse_type, horse_name, horse_speed):
        if horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
            return horse
        elif horse_type == 'Appaloosa':
            horse = Appaloosa(horse_name, horse_speed)
            return horse

    @staticmethod
    def __check_jockey_horse(jockey):
        if jockey.horse is not None:
            return True

    @staticmethod
    def _validate_jockey_not_in_race(jockey, race):
        for jock in race.jockeys:
            if jockey == jock:
                return True
            return False

    @staticmethod
    def __validate_participants_in_race(race):
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")

    @staticmethod
    def __race_horses(race):
        winner = None
        max_speed = 0
        for jockey in race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner = jockey
        return winner, max_speed
