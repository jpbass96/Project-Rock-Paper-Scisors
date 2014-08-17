import random
import time

class Bot:
	bot = None

	def BotInput(self):
		self.bot = random.randrange(1,3+1)

	def BotStatConversion(self):		

		if self.bot == 1:
			return ("Rock")

		if self.bot == 2:
			return ("Paper")

		if self.bot == 3:
			return ("Scissors")

	def GetBot(self):
		return (self.bot)