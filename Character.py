from Dice import Dice
import tables
import random
from prettytable import PrettyTable
import textwrap


class Character:

    def __init__(self,
                 name=None,
                 presence=None,
                 toughness=None,
                 agility=None,
                 strength=None,
                 hit_points=None,
                 omens=None,
                 silver=None,
                 background=None,
                 character_abilities=None
                 ):

        self.initialize_dice()
        self.initialize_attributes(
            name, presence, toughness, agility, strength, hit_points, omens, background, character_abilities)

    def initialize_dice(self):
        self.d2 = Dice(2)
        self.d4 = Dice(4)
        self.d6 = Dice(6)
        self.d8 = Dice(8)
        self.d10 = Dice(10)
        self.d12 = Dice(12)

    def initialize_attributes(self, name, presence, toughness, agility, strength, hit_points, omens, background, character_abilities):
        self.name = self.roll_name()
        self.inventory = []
        self.presence = self._set_ability(presence)
        self.toughness = self._set_ability(toughness)
        self.agility = self._set_ability(agility)
        self.strength = self._set_ability(strength)
        self.carrying_capacity = self.strength + 8
        self.hit_points = self.roll_hit_points()
        self.omens = self.roll_omens()
        self.character_class = "No class"
        self.silver = 0
        self.background = self.roll_background()
        self.character_abilities = self.roll_character_abilities()

    def roll_omens(self, d2=None):
        if d2 is None:
            d2 = self.d2.roll()
        return d2

    def roll_name(self, d6=None, d8=None):
        if d6 is None:
            d6 = self.d6.roll()
        if d8 is None:
            d8 = self.d8.roll()

        for entry in tables.names:
            if entry["d6"] == d6 and entry["d8"] == d8:
                return entry["Name"]
                break

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

    def set_initial_equipment(self, d1num=None, d2num=None, d3num=None):
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
            random_unclean_scroll = random.choice(
                list(tables.scrolls["Unclean Scrolls"].values()))
            self.inventory.append(random_unclean_scroll["Scroll"])
            self.inventory.remove("Unclean scroll")

        elif "Sacred scroll" in self.inventory:
            random_sacred_scroll = random.choice(
                list(tables.scrolls["Sacred Scroll"].values()))
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
                # Dividir en líneas de 50 caracteres
                wrapped_description = textwrap.fill(item_description, 50)
                table.add_row([self.inventory.index(item) +
                               1, item, wrapped_description])
            else:
                table.add_row([self.inventory.index(
                    item) + 1, item, item_description])

        print("\nInventory:\n")
        print(table)

    def show_abilities(self):
        table = PrettyTable()
        table.field_names = ["Ability", "Score"]

        table.align["Ability"] = "l"

        def format_ability_score(score):
            if score > 0:
                return f"+{score}"
            elif score < 0:
                return f"{score}"
            else:
                return "±0"

        table.add_row(["Agility", format_ability_score(self.agility)])
        table.add_row(["Presence", format_ability_score(self.presence)])
        table.add_row(["Strength", format_ability_score(self.strength)])
        table.add_row(["Toughness", format_ability_score(self.toughness)])

        print("\nAbilities:\n")
        print(table)

    def show_character_info(self):
        table = PrettyTable()
        table.header = False
        table.align = "l"

        table.add_row(["Name", self.name])
        table.add_row(["Class", self.character_class])
        table.add_row(["HP", self.hit_points])
        table.add_row(["Omens", self.omens])

        print("\nCharacter Info:\n")
        print(table)

    def print_character_sheet(self):
        self.show_character_info()
        self.show_abilities()
        self.show_inventory()

    def _get_item_info(self, item_name):
        for item_table in tables.initial_equipment.values():
            item_info = next(
                (item for item in item_table if item["name"] == item_name), None)
            if item_info:
                return item_info

        for scroll_table in tables.scrolls.values():
            scroll_info = next((scroll for scroll in scroll_table.values(
            ) if scroll["Scroll"] == item_name), None)
            if scroll_info:
                return {"description": scroll_info["Description"]}

        for weapon in tables.initial_weapons.values():
            if weapon["name"] == item_name:
                return weapon

        for armor in tables.initial_armors.values():
            if armor["name"] == item_name:
                return armor

        return {"description": ""}

    def set_initial_weapon(self, rolled_number=None):
        if rolled_number is None:
            rolled_number = self.d10.roll()
            for item in self.inventory:
                if "Unclean Scroll" in item or "Sacred Scroll" in item:
                    rolled_number = self.d6.roll()
                    break

        if rolled_number in tables.initial_weapons:
            weapon_name = tables.initial_weapons[rolled_number]["name"]
            self.inventory.append(weapon_name)

    def set_initial_armor(self, rolled_number=None):
        if rolled_number is None:
            rolled_number = self.d4.roll()
            for item in self.inventory:
                if "Unclean Scroll" in item or "Sacred Scroll" in item:
                    rolled_number = self.d2.roll()
                    break

        if rolled_number in tables.initial_armors:
            if rolled_number != 1:
                armor_name = tables.initial_armors[rolled_number]["name"]
                self.inventory.append(armor_name)

    def roll_hit_points(self, rolled_number=None):
        if rolled_number is None:
            rolled_number = self.d8.roll()

        hit_points = rolled_number + self.toughness
        return hit_points

        if hit_points < 1:
            hit_points = 1

    def roll_background(self, rolled_number=None):
        if rolled_number is None:
            return "Your past is a mistery"
        else:
            return "Your past is a mistery"

    def roll_character_abilities(self, rolled_number=None):
        if rolled_number is None:
            return "You do not have any special ability"
        else:
            return "You do not have any special ability"

