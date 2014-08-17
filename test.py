import time
import random
import GameBegin
import GameFlow
import player
import bot

PlayerObj = player.Player()
BotObj = bot.Bot()
GameFlowObj = GameFlow.Game()
GameStartObj = GameBegin.GameStart()



GameStartObj.Greeting()
GameStartObj.Intro()

GameFlowObj.play_game()
GameFlowObj.play_again()






