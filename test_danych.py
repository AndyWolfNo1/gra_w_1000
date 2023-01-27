import numpy as np
import matplotlib.pyplot as plt
from tysiac import *
import csv
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics

names = ['Marek', 'Stefan', 'Janusz', 'Bogdan']
players = [Player(name) for name in names]
talia_kart = Deck().take()
game = Game()
game.deal_the_cards(players)
game.step1()

win_player = game.players[game.max_auction_id[0]]

game.step2()

cards = win_player.cards

