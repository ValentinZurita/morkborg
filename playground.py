from Dice import Dice
from character import Character

dice = Dice(6)
print(dice.roll())
print(dice.roll_n_times(3))


player = Character('Paco', 9, 10)
print(player.agility)