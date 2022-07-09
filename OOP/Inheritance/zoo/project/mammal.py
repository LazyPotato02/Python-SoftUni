from .animal import Animal


class Mammal(Animal):

    def __init__(self, *args):
        super().__init__(*args)
