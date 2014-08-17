import GameFlow
import time
import random

GameFlow = GameFlow.game()


class Player:
	Score = 0
	Lives = 5

	def HumInput(self):
		correct = False
		while not correct:
			self.play = input("User Input Here: ")
			if self.play == ("1") or self.play == ("2") or self.play == ("3"):
				correct = True
				print (" ")


	def PlayerChanges(self):
		GameFlow.GetResults()

		if GameFlow.win == True:
			Score += 1
			
		if GameFlow.lose == True:
			Lives -= 1

	
	def GetScore(self):
		return (self.Score)

	def GetLives(self):
		return (self.Lives)

	def GetPlay(self):
		return (self.play)	



	def Status(self):
		print ("Lives: " + str(self.Lives))
		print ("Score: " + str(self.score))


	def HumStatConversion(self):
		if int(self.play) == 1:
			return ("Rock")

		if int(self.play) == 2:
			return ("Paper")

		if int(self.play) == 3:
			return ("Scissors")
			
			