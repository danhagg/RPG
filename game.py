# not from people import hero (see ***)
from people.hero import Hero
from people.goblin import Goblin
from people.zombie import Zombie

# *** not hero.Hero
hero = Hero(input("What is your hero's name? "))
opponent = Goblin("Dave")

while hero.alive() and opponent.alive():
    choice = input("\nWhat do you want to do?\na. fight\nb. do nothing\nc. flee\n")

    print("> ", end=' ')
    if choice == "a":

        # Hero attacks goblin
        r = hero.diceRoll()
        print(r)
        hero.attack(opponent, r)
    elif choice == "b":
        # Goblin attacks hero
        opponent.attack(hero)
    elif choice == "c":
        print("YOU RAN AWAY... CHICKEN")
        break
    else:
        print("Invalid input {}".format(choice))
