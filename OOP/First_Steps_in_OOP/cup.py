class Cup:
    def __init__(self, size: int, quantity: int,) -> None:
        self.size = size
        self.quantity = quantity

    def fill(self, value):
        cap = self.size
        fill = self.quantity + value
        if fill > cap:
            pass
        else:
            self.quantity = fill
    
    def status(self):
        return self.size - self.quantity

cup = Cup(100, 40)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
