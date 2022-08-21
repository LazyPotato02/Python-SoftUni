from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TYPE = 'Appaloosa'

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        try:
            self.speed += 2
        except ValueError:
            self.speed = self.MAX_SPEED

