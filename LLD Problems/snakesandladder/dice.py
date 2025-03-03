import random

class Dice:
    def __init__(self, dice_count):
        self.min = 1
        self.max = 6
        self.dice_count = dice_count

    def roll(self):
        total_sum = 0
        dice_used = 0
        while dice_used < self.dice_count:
            total_sum += random.randint(self.min, self.max)
            dice_used += 1

        return total_sum