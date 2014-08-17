import time
import random
import bot
import player

Player = player.Player()
Bot = bot.Bot()


class game:
	
	draw = False
	win = False
	lose = False

	def GetResults(self):
		return (self.draw)
		return (self.win)
		return (self.lose)
	
	def HumRules(self):
		print ("Press 1 for Rock")
		
		print ("Press 2 for Paper")
		
		print ("Press 3 for Scissors")
		time.sleep(.5)



	def CheckLose(self):
		Player.GetPlay()
		Bot.GetBot()

		if Bot.bot == 1 and int(Player.play) == 3:
			self.lose = True

		if Bot.bot == 2 and int(Player.play) == 1:
			self.lose = True


		if Bot.bot == 3 and int(Player.play) == 2:
			self.lose = True

	def CheckWin(self):
		Player.GetPlay()
		Bot.GetBot()

		if Bot.bot == 1 and int(Player.play) == 2:
			self.win = True
		
		if Bot.bot == 2 and int(Player.play) == 3:
			self.win = True

		if Bot.bot == 3 and int(Player.play) == 1:
			self.win = True

	def CheckDraw(self):
		Player.GetPlay()
		Bot.GetBot()

		if Bot.bot / int(Player.play) == 1:
			self.draw = True


	def DramaPlay(self):
		print ("Rock...")
		time.sleep(0.3)
		print ("Paper...")
		time.sleep(0.3)
		print ("Scissors...")
		time.sleep(0.3)
		print ("Shoot!")
		time.sleep(0.3)

	def GameResult(self):
		if self.win == True:
			print ("You Win!")

		if self.lose == True:
			print ("You Lose!")

		if self.draw == True:
			print ("You Draw!")


	

	def Stats(self):
		Player.HumStatConversion()
		Bot.BotStatConversion()

		
		print ("You Chose " +  str(Player.HumStatConversion()) + " and the bot chose " +  str(Bot.BotStatConversion()))
		
		Player.Status()
		
		print (" ")
		print (" ")
		time.sleep(1.5)


























