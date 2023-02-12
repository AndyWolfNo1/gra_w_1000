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
game.step2()
res = game.step3()

as1 = talia_kart[0]
dycha = talia_kart[1]
as2 = talia_kart[6]
as3 = talia_kart[12]
dama = talia_kart[3]
dupek = talia_kart[16]

wp = game.players[game.max_auction_id[0]]



def my_f():
    if len(game.players[0].cards) > 0:
        print('Ruch: ', game.moves)
        res = game.gameplay_result
        max_card, max_id = game.statistics.check_the_gameplay()
        print('rezultat gry; ', res)
        print('max_card, max_id: ', max_card.name,max_card.color, max_id)
        print('Karty:')
        for i in res[0]:
            print(i.name, i.color)
    else:
        print('brak kart')