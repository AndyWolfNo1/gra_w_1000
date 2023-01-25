import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class Card:
    """ Klasa definiuje kartę do gry, przyjmuje 2 argumenty. Pierwszy
        argument to nazwa karty ['9', 10', 'J', 'Q', 'K', 'A'].
        Drugi argument to liczba od 0-3 która definouje kolor karty.
        Kolory kart ['trefl', 'pik', 'kier', 'karo']"""
    
    names = {'9':0, '10':10, 'J':2, 'Q':3, 'K':4, 'A':11}
    colors = ['trefl', 'pik',
                        'kier', 'karo']

    def __init__(self, name, color_nr, nr):
        """Konstruktor klasy, definiuje wartość danej karty oraz kolor. """
        self.name = name
        self.value = self.names[name]
        self.color = self.colors[color_nr]
        self.id = nr
        
    def __lt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania < obiektów karty"""
        if self.value < other.value:
            return True
        return False

    def __gt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania > obiektów karty"""
        if self.value > other.value:
            return True
        return False

    def __repr__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu"""
        return str(self.id)
        #return self.name+' '+self.color

#    def __str__(self):
#        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu w obiekcie print()"""
#        return self.name+' '+self.color

    def __eq__(self, other):
        """ Metoda magiczna, sprawdza równość wartości obiektów"""
        if self.value == other.value:
            return True
        return False

    def __add__(self, other):
        """ Metoda magiczna, dodaje dwa obiekty"""
        return self.value + other.value

    def __sub__(self, other):
        """ Metoda magiczna, odejmuje dwa obiekty"""
        return self.value - other.value


class Deck:
    """Klasa definiująca talię, tworzy 24 karty do gry w 1000 """
    def __init__(self):
        self.names_c = ['A', '10', 'K', 'Q', 'J', '9']
        self.cards = []
        nr = 1
        for j in range(4):
            for i in self.names_c:
                self.cards.append(Card(i,j, nr))
                nr+=1

    def __str__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania
            obiektu w obiekcie print()"""
        return "Talia 24 kart do gry w tysiąca"

    def __repr__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu"""
        return "TALIA_24_obj"

    def take(self):
        """Metoda pozwala pobrać gotowa talie"""
        return self.cards


class Player:
    """Klasa definiuje gracza, przyjmuje tylko jeden argument, imię. """
    def __init__(self, name):
        self.ID = int()
        self.colors = {'trefl': 100, 'pik' : 80, 'kier': 60, 'karo': 40}
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        """ Metoda magiczna, wyświetla nazwę podczas wywołania obiektu"""
        return self.name

    def sorted_cards(self):
        self.cards = sorted(self.cards, key=lambda card: card.id, reverse=False)

        suma = 0
        for i in range(len(self.cards)):
            suma += self.cards[i].value
        self.sum_points = suma
        
    def create_cards_array(self):
        self.array_cards = np.zeros((24))
        for card in self.cards:
            self.array_cards[card.id-1]=1

    def create_colors_array(self, colors):
        self.array_colors = colors
   
    def take_card(self, cards, musik = None):
        if musik == None:
            self.cards = cards
            self.sorted_cards()
            self.create_cards_array()
        if musik == True:
            self.cards += cards

    def print_cards(self):
        buf = []
        for i in range(len(self.cards)):
            name = self.cards[i].name+'  '+self.cards[i].color
            buf.append(name)
        print(buf)

    def gen_auction(self):
        buff = []
        c = 1.
        suma = 0.
        res = self.array_cards.reshape(4,6)
        for i in range(4):
            buff.append(list(res[i]))
        for i in range(4):
            #redukcja dziewiątek
            buff[i][5] = 0.
            buff[i][4] = 0.
            #dodawanie wartoci koloru
            buff[i].append(self.array_colors[i])
            suma += sum(buff[i])*c
            c -= 0.20
        self.auction = round(suma, 3)

class Game:
    _instance = None
    title ="A_trefl,10_trefl,K_trefl,D_trefl,J_trefl,9_trefl,A_pik,10_pik,K_pik,D_pik,J_pik,9_pik,A_kier,10_kier,K_kier,D_kier,J_kier,9_kier,A_karo,10_karo,K_karo,D_karo,J_karo,9_karo,trefl,pik,kier,karo\n"
    index = title.split(',')
    indexs = index[:-4]


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.players = []
        self.perceptron()
        
    def suffle_cards(self):
        self.new_cards = Deck().take()
        shuffled_cards = []
        while len(self.new_cards) > 0:
            index = random.randint(0, len(self.new_cards) - 1)
            shuffled_cards.append(self.new_cards[index])
            self.new_cards.pop(index)
        return shuffled_cards

    def deal_the_cards(self, players):
        self.players_name = [self.players[i].name for i in range(len(self.players))]
        self.players_cards = [self.players[i].cards for i in range(len(self.players))]
        self.s_cards = self.suffle_cards()
        order_of_hands = [[self.s_cards[0], self.s_cards[1],
                           self.s_cards[9], self.s_cards[10],
                           self.s_cards[19]],
                          [self.s_cards[2], self.s_cards[3],
                           self.s_cards[12], self.s_cards[13],
                           self.s_cards[20]],
                          [self.s_cards[4], self.s_cards[6],
                           self.s_cards[14], self.s_cards[15],
                           self.s_cards[21]],
                          [self.s_cards[7], self.s_cards[8],
                           self.s_cards[16], self.s_cards[18],
                           self.s_cards[22]]]

        self.players = players
        self.musik = []
        # 5, 11, 17, 23
        self.musik.append(self.s_cards[5::6])
        self.musik = sorted(self.musik[0], key=lambda card: card.id, reverse=False)
        
        for i in range(4):
            self.players[i].take_card(order_of_hands[i])
            self.players[i].ID = i
        self.predict_players()
    
    def perceptron(self):
        index = self.title.split(',')
        self.indexs = index[:-4]
        df = pd.read_csv('data.csv')
        color_column = ['trefl', 'pik', 'kier', 'karo']
        X = df[self.indexs]
        y = df[color_column]
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

    def predict_players(self):
        for i in range(len(self.players)):
            pc = self.players[i].array_cards
            pc = pc.reshape(1,24)
            pc = pd.DataFrame(pc, columns=self.indexs)
            y_pred = self.model.predict(pc)
            self.players[i].create_colors_array(y_pred[0])
            self.players[i].gen_auction()
            
    def auction(self):
        self.auction = dict()
        for i in range(4):
            self.auction[self.players[i].ID] = self.players[i].auction
        maximum = max([x for x in self.auction.values()])
        self.max_auction_id = [key for key, value in self.auction.items() if value == maximum]

    def step1(self):
        self.auction()
        if len(self.max_auction_id)==1:
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()
        else:
            #do poprawy
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()


class Statistics:
    pass
