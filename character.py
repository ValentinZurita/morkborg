from Dice import Dice
import tables


class Character():
	def __init__(self, name, presence, toughness, agility=None):
		self.name = name
		self.presence = presence
		self.toughness = toughness
		self.d6 = Dice(6)

		if agility is None:
			self.agility = self.set_agility()
		else:
			self.agility = agility

	def roll_ability(self):
		die1 = self.d6.roll()
		die2 = self.d6.roll()
		die3 = self.d6.roll()
		die4 = self.d6.roll()

		lowest_dice = min(die1, die2, die3, die4)

		acumulated = die1 + die2 + die3 + die4 - lowest_dice

		return acumulated


	def set_agility(self):
		rolled_number = self.roll_ability()
		score = self.get_ability_score(rolled_number)
		return score


	def get_ability_score(self, rolled_number):
		score = None
		for rolled_range, value in tables.abilities_score.items():
		    if rolled_range[0] <= rolled_number <= rolled_range[1]:
		        score = value
		        break
		return score


 
