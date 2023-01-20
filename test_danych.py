import numpy as np
from tysiac import *
<<<<<<< HEAD
from perceptrons import Perceptron
import csv
=======
import csv
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
>>>>>>> 9ac6399 (zmiany liczenia pkt, dodano perceptron)

names = ['Marek', 'Stefan', 'Janusz', 'Bogdan']
players = [Player(name) for name in names]
cards = Deck().take()
game = Game()
game.deal_the_cards(players)
<<<<<<< HEAD
statistics = Statistics(game)

def write_result(data):
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file)
        file.write("card1,card2,card3,card4,card5,result\n")
        write.writerows(data) 

def rozegraj_gre():
    game.deal_the_cards(players)
    for i in range(4):
        res1 = game.players[i].amount_point_pairs
        res2 = game.players[i].trefl_points_random_forest_classifier
        if res1 != res2:
            print(game.players[i].print_cards())
            game.players[i].cards.append(game.players[i].amount_point_pairs)
            data.append(game.players[i].cards)
            print(game.players[i].amount_point_pairs)
            print(game.players[i].trefl_points_random_forest_classifier)
                        
def testing():
    data = []
    for i in range(10000):
        bledy = len(data)
        print('--'*3, 'wykonano', i, 'grę', '--'*3, 'błędy:', bledy, '--'*3)
        rozegraj_gre()
    write_result(data)


card1 = cards[0]
card2 = cards[6]
card3 = cards[12]
card4 = cards[18]
card5 = cards[22]

game.players[0].take_card([card1, card2, card3, card4, card5])

gc = game.players[0].cards

pred = np.arange(10, 210, 10)
=======
#statistics = Statistics(game)
card1 = cards[2]
card2 = cards[3]
card3 = cards[8]
card4 = cards[9]
card5 = cards[22]
cards5 = [card1,card2,card3,card4,card5]

#game.players[0].take_card([card1, card2, card3, card4, card5])
title ="A_trefl,10_trefl,K_trefl,D_trefl,J_trefl,9_trefl,A_pik,10_pik,K_pik,D_pik,J_pik,9_pik,A_kier,10_kier,K_kier,D_kier,J_kier,9_kier,A_karo,10_karo,K_karo,D_karo,J_karo,9_karo,trefl,pik,kier,karo"
index = title.split(',')
indexs = index[:-4]
colors = index[-4:]

def generator_danych(iters=100):
    data_good = []
    data_bad = []
    for i in range(iters):
        game.deal_the_cards(players)
        for player in game.players:
            if len(player.pairs) > 0:
                array1 = np.append(player.array_cards, player.array_colors_cards)
                data_good.append(array1)
            else:
                array1 = np.append(player.array_cards, player.array_colors_cards)
                data_bad.append(array1)
    print(len(data_good))
    print(len(data_bad[::9]))
    data = data_good + data_bad[::5]
    random.shuffle(data)
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file)
        file.write(title)
        write.writerows(data) 
    return data

