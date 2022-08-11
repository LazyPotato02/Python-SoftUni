from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = list()
        self.drivers = list()
        self.races = list()

    def create_car(self, car_type: str, model: str, speed_limit: int):

        car = self.__initialize_car(car_type, model, speed_limit)
        self.__check_if_car_exists(model)

        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver = Driver(driver_name)
        self.__check_if_driver_exists(driver_name)
        if driver:
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race = Race(race_name)
        self.__check_if_race_exists(race_name)
        if race:
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.__find_driver(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__find_car(car_type)
        if not car.is_taken and driver.car is not None:
            retval = f"Driver {driver_name} changed his car from {driver.car.model} to {car.model}."
            self.cars.append(driver.car)
            driver.car = car
            car.is_taken = True
            return retval
        if not car.is_taken and driver.car is None:
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.__find_race(race_name)

        driver = self.__find_driver(driver_name)
        self.__raise_if_driver_is_missing(driver, driver_name)
        self.__check_if_driver_has_car(driver)
        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        if race and driver.car:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__find_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        retval = ''
        if race and len(race.drivers) >= 3:
            race_results = sorted(race.drivers, key=lambda item: -item.car.speed_limit)[:3]
            for driver in race_results:
                driver.add_win()
                retval += f"Driver {driver.name} " \
                          f"wins the {race_name} race " \
                          f"with a speed of {driver.car.speed_limit}.\n"
            return retval.strip()
        raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def __initialize_car(car_type, model, speed_limit):
        if car_type == 'SportsCar':
            car = SportsCar(model, speed_limit)
            return car
        elif car_type == 'MuscleCar':
            car = MuscleCar(model, speed_limit)
            return car
        return None

    def __check_if_car_exists(self, model):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

    def __check_if_driver_exists(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

    def __check_if_race_exists(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

    def __find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_car(self, car_type):
        # car_ll = reversed(self.cars)
        for car in reversed(self.cars):
            if car.MODEL == car_type:
                c_idx = self.cars.index(car)
                self.cars.pop(c_idx)
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def __find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    @staticmethod  # May cause errors
    def __raise_if_driver_is_missing(driver, driver_name):
        if driver is None:
            raise Exception(f"Race {driver_name} could not be found!")

    @staticmethod
    def __check_if_driver_has_car(driver):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")
