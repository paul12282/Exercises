import random

class Dice:
    def roll(self):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        return dice_one, dice_two


player = Dice()
print(player.roll())