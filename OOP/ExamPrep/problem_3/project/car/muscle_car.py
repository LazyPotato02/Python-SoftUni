from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450
    MODEL = 'MuscleCar'
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

