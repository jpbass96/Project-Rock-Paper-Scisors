import time
import random
import bot
import player

PlayerObj = player.Player()
BotObj = bot.Bot()


class Game:
	def __init__(self):
		self.lose = False
		self.win = False
		self.draw = False


	
	def hum_rules(self):
		print ("Press 1 for Rock")
		
		print ("Press 2 for Paper")
		
		print ("Press 3 for Scissors")

		time.sleep(.5)


	def get_inputs(self):	

		PlayerObj.HumInput()
		BotObj.BotInput()



	def check_lose(self):
		PlayerObj.GetPlay()
		BotObj.GetBot()

		if BotObj.GetBot() == 1 and int(PlayerObj.GetPlay()) == 3:
			self.lose = True

		if BotObj.GetBot() == 2 and int(PlayerObj.GetPlay()) == 1:
			self.lose = True


		if BotObj.GetBot() == 3 and int(PlayerObj.GetPlay()) == 2:
			self.lose = True

	def check_win(self):
		PlayerObj.GetPlay()
		BotObj.GetBot()

		if BotObj.GetBot() == 1 and int(PlayerObj.GetPlay()) == 2:
			self.win = True
		
		if BotObj.GetBot() == 2 and int(PlayerObj.GetPlay()) == 3:
			self.win = True

		if BotObj.GetBot() == 3 and int(PlayerObj.GetPlay()) == 1:
			self.win = True

	def check_draw(self):
		PlayerObj.GetPlay()
		BotObj.GetBot()

		if BotObj.bot / int(PlayerObj.GetPlay()) == 1:
			self.draw = True


	def drama_play(self):
		print ("Rock...")
		time.sleep(0.3)
		print ("Paper...")
		time.sleep(0.3)
		print ("Scissors...")
		time.sleep(0.3)
		print ("Shoot!")
		time.sleep(0.3)
		print (" ")

	def game_result(self):
		if self.win == True:
			print ("You Win!")
			PlayerObj.score_change()

		if self.lose == True:
			print ("You Lose!")
			PlayerObj.lives_change()

		if self.draw == True:
			print ("You Draw!")


	

	def stats(self):
		PlayerObj.HumStatConversion()
		BotObj.BotStatConversion()

		
		print ("You Chose " +  str(PlayerObj.HumStatConversion()) + " and the bot chose " +  str(BotObj.BotStatConversion()))
		
		PlayerObj.Status()
		
		print (" ")
		print (" ")
		time.sleep(1.5)



	def whole_game(self):
		self.reset_result()
		self.hum_rules()

		self.get_inputs()

		self.check_win()
		self.check_lose()
		self.check_draw()

		self.drama_play()

		self.game_result()
		self.stats()

	def reset_result(self):
		self.win = False
		self.lose = False
		self.draw = False


	def play_game(self):
		PlayerObj.GetLives()
		while PlayerObj.lives > 0:
			self.whole_game()


	def play_again(self):		
			
		good_input = False

		while not good_input:
			print ("Would you like to restart?")
			print ("Type Yes or No")
			restart = input("User Input Here: ")
			if restart == ("No"):
				print ("Thank you for playing Bass RPS!")
				good_input = True
			if restart == ("Yes"):
				print ("Restarting Game")
				print (" ")
				PlayerObj.reset_life()
				PlayerObj.reset_score()
				self.play_game()




























