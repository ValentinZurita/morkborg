import random

class Dice:
	def __init__(self, dnumber):
		self.dnumber = dnumber

	def roll(self):
		rolled_number = random.randint(1, self.dnumber)
		return rolled_number

	def roll_n_times(self, n_times):
		acumulated = 0
		for n in range(n_times):
			acumulated = self.roll() + acumulated
		return acumulated
		