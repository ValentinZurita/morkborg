from Dice import Dice
from character import Character



player = Character('Paco')
print("Agility:" + str(player.agility))
print("toughness:" + str(player.toughness))
print("presence:" + str(player.presence))
print("strenght:" + str(player.strength))
print("Inventory:" + str(player.carrying_capacity))

player.set_random_equipment()
player.show_inventory()