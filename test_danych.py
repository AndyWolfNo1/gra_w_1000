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
title = "A_trefl,10_trefl,K_trefl,D_trefl,J_trefl,9_trefl,A_pik,10_pik,K_pik,D_pik,J_pik,9_pik,A_kier,10_kier,K_kier,D_kier,J_kier,9_kier,A_karo,10_karo,K_karo,D_karo,J_karo,9_karo,trefl,pik,kier,karo\n"
players = [Player(name) for name in names]
cards = Deck().take()
game = Game()
game.deal_the_cards(players)

def write_result(data):
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file)
        file.write(title)
        write.writerows(data) 
        

def check_error(game, iters=1000):
    errors = 0
    res_return = []
    res_colors = []
    bad_colors = []
    for i in range(iters):
        game.deal_the_cards(players)
        game.step1()
        cards = game.players[game.max_auction_id[0]].reshape_cards
        colors = game.players[game.max_auction_id[0]].array_colors
        colors_res = [0.,0.,0.,0.]
        #print("typ cards:", type(cards), "typ colors:", type(colors), "typ colors_res:", type(colors_res))
        for j in range(4):
            if cards[j][2]+cards[j][3] == 2.0:
                colors_res[j]= 1.0
                for m in range(4):
                    if colors_res[m]!=colors[m]:
                        print(game.players[game.max_auction_id[0]].print_cards(), colors_res[m],colors[m] , colors_res, colors)
                        errors += 1
                        res_return.append(game.players[game.max_auction_id[0]].array_cards)
                        res_colors.append(colors_res)
                        bad_colors.append(colors)
        print('błędy:', errors)
        print("iteracja:", i)
    return res_return, res_colors, bad_colors

def scal_dane(res_return, res_colors):
    res = []
    res2 =[]
    if len(res_return) > 0:
        for i in range(len(res_return)):
            res.append(list(res_return[i]))
        for i in range(len(res)):
            res3 = res[i]+res_colors[i]
            res2.append(res3)
        return res2
    else:
        return 0

def percep():
    df = pd.read_csv('data.csv')
    color_column = ['trefl', 'pik', 'kier', 'karo']
    index = title.split(',')
    indexs = index[:-4]
    X = df[indexs]
    y = df[color_column]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    iters = 0
    for row in y_test.itertuples():
        print(row.trefl, row.pik, row.kier, row.karo, y_pred[iters])
        iters+=1
        
        
      
#res_return, res_colors, bad_colors = check_error(game)

#res = scal_dane(res_return, res_colors)
game.step1()
print(game.players[game.max_auction_id[0]].print_cards() ,game.players[game.max_auction_id[0]].array_colors)