

import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomStop:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:

            if random.randint(0, 1) == 0:  # randomly decides if it will continue or stop
                diceRollResults = zombiedice.roll()
            else:
                break


class TwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains >= 2:  # stops rolling after it has rolled two brains
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class TwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun >= 2:  # stops rolling after it has rolled two shotguns
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class OneFourTwoShot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        rolls = 0
        one_to_four = random.randint(0, 3)
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            rolls += 1
            if rolls <= one_to_four:  # initially decides it’ll roll the dice one to four times
                if shotgun==2:  # will stop early if it rolls two shotguns
                    break
                else:
                    diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class ShotgunsOverBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            print(f"{brains} brains")
            print(f"{shotguns} shotguns")
            if shotguns>brains:  # stops rolling after it has rolled more shotguns than brains
                break
            else:
                diceRollResults = zombiedice.roll()


zombies = (
    RandomStop(name='Randombot'),
    TwoBrains(name='Twobrainbot'),
    TwoShotguns(name='2shotgundonebot'),
    OneFourTwoShot(name='nomorethan2bot'),
    ShotgunsOverBrains(name='Shotgunoverbbot'),
    
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)