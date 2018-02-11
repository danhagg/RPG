from people.enemy import Enemy
import math
class Zombie(Enemy):
    def __init__(self, name):
        self.name = name
        self.power = math.inf
        self.health = 10
