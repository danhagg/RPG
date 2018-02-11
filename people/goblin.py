from people.enemy import Enemy

class Goblin(Enemy):
    def __init__(self, name):
        self.name = name
        self.power = 2
        self.health = 6
