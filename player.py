
import time
import random





class Player:

	def __init__(self):
		self.score = 0
		self.lives = 5

	def HumInput(self):
		correct = False
		while not correct:
			self.play = input("User Input Here: ")
			if self.play == ("1") or self.play == ("2") or self.play == ("3"):
				correct = True
				print (" ")


	def score_change(self):
		self.score += 1

	def lives_change(self):
		self.lives -= 1



	
	def GetScore(self):
		return (self.score)

	def GetLives(self):
		return (self.lives)

	def GetPlay(self):
		return (self.play)	



	def Status(self):
		print ("Lives: " + str(self.lives))
		print ("Score: " + str(self.score))


	def HumStatConversion(self):
		if int(self.play) == 1:
			return ("Rock")

		if int(self.play) == 2:
			return ("Paper")

		if int(self.play) == 3:
			return ("Scissors")


	def reset_life(self):
		self.lives += 5

	def reset_score(self):
		self.score -= self.score


			
			