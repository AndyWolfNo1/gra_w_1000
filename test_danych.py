import numpy as np
import matplotlib.pyplot as plt
from tysiac import *
import csv
import pandas as pd
import random
import json

names = ['Marek', 'Stefan', 'Janusz']
players = [Player(name) for name in names]
talia_kart = Deck().take()

p1 = players[0]
p2 = players[1]
p3 = players[2]

table = Table()
game = Game()
game1 = Game()
game2 = Game()
game1.add_player(players[0])
game1.add_player(players[1])
table.add_game(game, p1)
table.add_game(game1, p2)
table.add_game(game2, p3)

table.activate_game_by_id(game1.ID)
table.activate_game_by_id(game2.ID)
res = table.return_active_games()


