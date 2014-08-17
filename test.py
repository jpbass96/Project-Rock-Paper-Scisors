import time
import random
import GameBegin
import GameFlow
import player
import bot

Player = player.Player()
Bot = bot.Bot()
GameFlow = GameFlow.game()
GameStart = GameBegin.GameStart()



GameStart.Greeting()
GameStart.Intro()

while Player.Lives > 0:
	GameFlow.win = False
	GameFlow.lose = False
	GameFlow.draw = False

	GameFlow.HumRules()

	Player.HumInput()
	Bot.BotInput()

	GameFlow.DramaPlay()

	GameFlow.CheckWin()
	GameFlow.CheckLose()
	GameFlow.CheckDraw()

	Player.PlayerChanges()

	GameFlow.GameResult()
	GameFlow.Stats()







