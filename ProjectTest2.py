import time
import random

lives = [1,2,3,4,5]
score = []
ready = False
alive = True


print ("Welcome to Bass RPS. This is a basic Rock, Paper, Scissors game played against a lone computer opponent.")
print ("You will have 5 lives and each time you lose a round, you will lose one life. Good Luck!")
print ("")
time.sleep(.5)
print ("Type ready when you are ready to begin.")

while not ready:
	start = input("User Input: ")
	if start == ("ready"):
		ready = True

while alive:
	print ("You currently have " + str(len(lives)) + " lives remaining")
	time.sleep(1)
	print ("Enter 1 for Rock")
	print ("Enter 2 for Scissors")
	print("Enter 3 for Paper")

	play = input("User Input: ")

	bot = random.randrange(1,3+1)

	print ("Rock...")
	time.sleep(.5)
	print ("Paper...")
	time.sleep(.5)
	print ("Scissors...")
	time.sleep(.5)
	print ("Shoot!")
	time.sleep(.5)


	print ("BOT: " + str(bot) + "PLAYER: " + str(play))


	if bot / int(play) == 1:
		print ("Draw")
		print ("Score: " + str(len(score)))

	if bot == 1 and int(play) == 2:

		print ("You Win!")
		score.append (len(score) + 1)
		print ("Score: " + str(len(score)))

	if bot == 1 and int(play) == 3:
		print ("You Lose!")
		del lives [len(lives) - 1:]
		print ("Score: " + str(len(score)))

	if bot == 2 and int(play) == 1:

		print ("You Lose!")
		del lives [len(lives) - 1:]
		print ("Score: " + str(len(score)))

	if bot == 2 and int(play) == 3:

		print ("You Win!")
		score.append (len(score) + 1)
		print ("Score: " + str(len(score)))

	if bot == 3 and int(play) == 1:

		print ("You Win!")
		score.append (len(score) + 1)
		print ("Score: " + str(len(score)))

	if bot == 3 and int(play) == 2:

		print ("You Lose!")
		del lives [len(lives) - 1:]
		print ("Score: " + str(len(score)))

	if len(lives) == 0:
		print ("Game Over!")
		print(len(score))
		alive = False
	



print ("Thanks for playing!")








