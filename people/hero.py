import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.power = 5
        self.health = 10

    def alive(self):
        if self.health > 0:
            return True
        else:
            print("{} died".format(self.name))

    def attack(self, goblin, r=1):
        goblin.health = goblin.health - self.power*r
        print("{0} attacks {1} and removes {2} health".format(self.name, goblin.name, self.power))

    def __str__(self):
        # add if statement here based upon health
        return "{}\n Power: {} &  Health: {}".format(self.name, self.power, self.health)

    def diceRoll(self):
        roll = 0
        min = 1
        max = 6
        roll = random.randint(min, max)
        return roll
        print("Rolling the dice... You rolled a {0}".format(roll))
