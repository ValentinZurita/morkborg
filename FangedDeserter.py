from Character import Character
import tables
from prettytable import PrettyTable
import textwrap

class FangedDeserter(Character):

    # Built like a Bull, roll 3d6+2 for Strength.

    # Begins with 2d6 × 10s and d2 Omens.

    # HP: Toughness + d10

    # Not a Bright Spark, roll 3d6-1 for Agility and Presence.

    def __init__(
        self,
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

        super().__init__(
            name,
            presence,
            toughness,
            agility,
            strength,
            hit_points,
            omens,
            silver,
            background,
            character_abilities
        )

        self.background = self.roll_background()


    ##Functions

    def roll_background(self, rolled_number=None):
        if rolled_number is None:
            rolled_number = self.d6.roll()

        background = tables.fanged_deserter["background"]
        earliest_memory = tables.fanged_deserter["earliest memories"][rolled_number]
        background = f"BACKGROUND: {background} \n\nYOUR ELDEST MEMORY IS: {earliest_memory}"

        return background

    def print_background(self):
        table = PrettyTable()
        table.header = False
        table.align = "l"

        background_lines = self.background.split('\n')
        for line in background_lines:
            wrapped_lines = textwrap.fill(line, width=70).split('\n')
            for wrapped_line in wrapped_lines:
                table.add_row([wrapped_line])

        print(table)


    def roll_class_abilities(self, rolled_number = None):
        if rolled_number is None:
            rolled_number = self.d6.roll()

        class_abilities = tables.fanged_deserter["optional abilities"][rolled_number]


