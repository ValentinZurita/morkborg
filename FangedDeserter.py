from Character import Character
import tables


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


    def print_hello(self): 
    	print("Hello from FangedDeserter")


    def roll_background(self, d6=None):
        if d6 is None:
            d6 = self.d6.roll()

        for entry, value in tables.fanged_deserter.items():
            print(entry, value)


