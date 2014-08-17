import time
import random

class GameStart:

	def Greeting(self):
		print ("Welcome to Bass RPS. This is a basic Rock, Paper, Scissors game played against a lone computer opponent.")
		time.sleep(.5)
		print ("You will have 5 lives and each time you lose a round, you will lose one life. Good Luck!")
		print ("")
		time.sleep(.5)
		print ("Type ready when you are ready to begin.")
		time.sleep(.5)



	def Intro(self):
		ready = False
		while not ready:
			start = input("User Input Here: ")
			if start == ("ready"):
				ready = True
				print (" ")



