from Dice import Dice
import tables
import random
from prettytable import PrettyTable
import textwrap


class Character:
    def __init__(self, name, presence=None, toughness=None, agility=None, strength=None):
        self.name = name
        self.d2 = Dice(2)
        self.d4 = Dice(4)
        self.d6 = Dice(6)
        self.d12 = Dice(12)
        self.d10 = Dice(10)
        self.presence = self._set_ability(presence)
        self.toughness = self._set_ability(toughness)
        self.agility = self._set_ability(agility)
        self.strength = self._set_ability(strength)
        self.carrying_capacity = self.strength + 8
        self.inventory = []

    def _roll_ability(self):
        return sum(sorted(self.d6.roll() for _ in range(4))[1:])

    def _set_ability(self, ability_value):
        return ability_value if ability_value is not None else self._generate_random_ability()

    def _generate_random_ability(self):
        rolled_number = self._roll_ability()
        score = self.set_ability_score(rolled_number)
        return score

    def set_ability_score(self, rolled_number):
        for rolled_range, value in tables.abilities_score.items():
            if rolled_range[0] <= rolled_number <= rolled_range[1]:
                return value
        return None

    def set_random_equipment(self):

        self.set_initial_equipment()
        self.set_initial_weapon()
        self.set_initial_armor()


    def set_initial_equipment(self, d1num=None, d2num =  None, d3num = None):
        if d1num is None:
            d1num = self.d6.roll()
        if d2num is None:
            d2num = self.d12.roll()
        if d3num is None:
            d3num = self.d12.roll()

        d1_list = tables.initial_equipment["1st"][d1num - 1]
        d2_list = tables.initial_equipment["2nd"][d2num - 1]
        d3_list = tables.initial_equipment["3rd"][d3num - 1]

        if d1_list["name"] != "Nothing":
            self.inventory.append(d1_list["name"])
        self.inventory.append(d2_list["name"])
        self.inventory.append(d3_list["name"])

        if "Unclean scroll" in self.inventory:
            random_unclean_scroll = random.choice(list(tables.scrolls["Unclean Scrolls"].values()))
            self.inventory.append(random_unclean_scroll["Scroll"])
            self.inventory.remove("Unclean scroll")

        elif "Sacred scroll" in self.inventory:
            random_sacred_scroll = random.choice(list(tables.scrolls["Sacred Scroll"].values()))
            self.inventory.append(random_sacred_scroll["Scroll"])
            self.inventory.remove("Sacred scroll")


    def show_inventory(self):
        table = PrettyTable()
        table.field_names = ["No.", "Item", "Description"]

        table.align["Item"] = "l"
        table.align["Description"] = "l"
        
        for item in self.inventory:
            item_info = self._get_item_info(item)
            item_description = item_info.get("description", "")
            if len(item_description) > 50:
                wrapped_description = textwrap.fill(item_description, 50)  # Dividir en líneas de 50 caracteres
                table.add_row([self.inventory.index(item) + 1, item, wrapped_description])
            else:
                table.add_row([self.inventory.index(item) + 1, item, item_description])
        
        print("\nInventory:\n")
        print(table)

    def _get_item_info(self, item_name):
        for item_table in tables.initial_equipment.values():
            item_info = next((item for item in item_table if item["name"] == item_name), None)
            if item_info:
                return item_info

        for scroll_table in tables.scrolls.values():
            scroll_info = next((scroll for scroll in scroll_table.values() if scroll["Scroll"] == item_name), None)
            if scroll_info:
                return {"description": scroll_info["Description"]}

        for weapon in tables.initial_weapons.values():
            if weapon["name"] == item_name:
                return weapon

        for armor in tables.initial_armors.values():
            if armor["name"] == item_name:
                return armor

        return {"description": ""}


    def set_initial_weapon(self, rolled_number = None):
        if rolled_number is None:
            rolled_number = self.d10.roll()
            for item in self.inventory:
                if "Unclean Scroll" in item or "Sacred Scroll" in item:
                    rolled_number = self.d6.roll()
                    break
 
        if rolled_number in tables.initial_weapons:
            weapon_name = tables.initial_weapons[rolled_number]["name"]
            self.inventory.append(weapon_name)


    def set_initial_armor(self, rolled_number = None):
        if rolled_number is None:
            rolled_number = self.d4.roll()
            for item in self.inventory:
                if "Unclean Scroll" in item or "Sacred Scroll" in item:
                    rolled_number = self.d2.roll()
                    break
 
        if rolled_number in tables.initial_armors:
            if rolled_number is not 1:
                armor_name = tables.initial_armors[rolled_number]["name"]
                self.inventory.append(armor_name)






    







