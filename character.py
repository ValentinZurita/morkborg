from Dice import Dice
import tables


class Character:
    def __init__(self, name, presence=None, toughness=None, agility=None):
        self.name = name
        self.d6 = Dice(6)
        self.presence = self._set_ability(presence)
        self.toughness = self._set_ability(toughness)
        self.agility = self._set_ability(agility)

    def _roll_ability(self):
        return sum(sorted(self.d6.roll() for _ in range(4))[1:])

    def _set_ability(self, ability_value):
        return ability_value if ability_value is not None else self._generate_random_ability()

    def _generate_random_ability(self):
        rolled_number = self._roll_ability()
        score = self._get_ability_score(rolled_number)
        return score

    def _get_ability_score(self, rolled_number):
        for rolled_range, value in tables.abilities_score.items():
            if rolled_range[0] <= rolled_number <= rolled_range[1]:
                return value
        return None
