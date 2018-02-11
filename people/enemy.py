class Enemy:
    def __init__(self, name):
        self.name = name

    def alive(self):
        if self.health > 0:
            return True
        else:
            print("{} died".format(self.name))

    def attack(self, hero):
        hero.health = hero.health - self.power
        print("{0} attacks {1} and removes {2} health".format(self.name, hero.name, self.power))

    def __str__(self):
        # add if statement here based upon health
        return "{}\n Power: {} &  Health: {}".format(self.name, self.power, self.health)
