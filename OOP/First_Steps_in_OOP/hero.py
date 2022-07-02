class Hero:
    def __init__(self,name, health) -> None:
        self.name = name
        self.health = health

    def heal(self, value):
        self.health += value
        
    def defend(self , value):
        self.health -= value
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))