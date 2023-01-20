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
        self.array_card = 1

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

    def check_pairs(self):
        result = []
        points = 0
        for color in self.colors:
            res = 0
            for card in self.cards:
                if card.color == color and card.name == "K":
                    res += 4
                elif card.color == color and card.name == "Q":
                    res += 3
                if res == 7:
                    result.append(color)
                    points += self.colors[color]
                    res = 0
        self.pairs = result
        self.points_pairs = points

        if len(self.pairs) > 0:
            for color in self.pairs:
                sumc = sum(card.value for card in self.cards if card.color == color)
                self.sum_colors = {color: sumc}
        else:
            self.sum_colors = 0

        amount = 0
        for i in range(len(self.cards)):
            amount += self.cards[i].value
        self.amount_points = amount

        self.amount_point_pairs = sum([self.colors[i] for i in self.pairs])

    def create_colors_array(self, colors):
        self.array_colors = colors
   
    def take_card(self, cards, musik = None):
        if musik == None:
            self.cards = cards
            self.check_pairs()
            self.sorted_cards()
            self.create_cards_array()

    def print_cards(self):
        buf = []
        for i in range(len(self.cards)):
            name = self.cards[i].name+'  '+self.cards[i].color
            buf.append(name)
        print(buf)


    def calc_coefficient(self):
        self.coefficient = 0
        
        def check_number_card(cards, nr):
            for i in range(len(cards)):
                if cards[i].id == nr:
                    return True
            else:
                return False
            
        for pair in self.pairs:
            if pair == 'trefl':
                if check_number_card(self.cards, 1)==True and check_number_card(self.cards, 2)==True:
                    self.coefficient += 130
                elif check_number_card(self.cards, 1)==True or check_number_card(self.cards, 2)==True:
                    self.coefficient += 110
            if pair == 'pik':
                if check_number_card(self.cards, 7)==True and check_number_card(self.cards, 8)==True:
                    self.coefficient += 100
                elif check_number_card(self.cards, 7)==True or check_number_card(self.cards, 8)==True:
                    self.coefficient += 90
            if pair == 'kier':
                if check_number_card(self.cards, 13)==True and check_number_card(self.cards, 14)==True:
                    self.coefficient += 80
                elif check_number_card(self.cards, 13)==True or check_number_card(self.cards, 14)==True:
                    self.coefficient += 70
            if pair == 'karo':
                if check_number_card(self.cards, 19)==True and check_number_card(self.cards, 20)==True:
                    self.coefficient += 60
                elif check_number_card(self.cards, 19)==True or check_number_card(self.cards, 20)==True:
                    self.coefficient += 50
            

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
        order_of_hands = [[self.s_cards[1], self.s_cards[2],
                           self.s_cards[10], self.s_cards[11],
                           self.s_cards[20]],
                          [self.s_cards[3], self.s_cards[4],
                           self.s_cards[13], self.s_cards[14],
                           self.s_cards[21]],
                          [self.s_cards[5], self.s_cards[7],
                           self.s_cards[15], self.s_cards[16],
                           self.s_cards[22]],
                          [self.s_cards[8], self.s_cards[9],
                           self.s_cards[17], self.s_cards[19],
                           self.s_cards[23]]]

        self.players = players
        self.musik = []
        self.musik.append(self.s_cards[6:19:6])
        self.musik = sorted(self.musik[0], key=lambda card: card.id, reverse=False)
        
        for i in range(4):
            self.players[i].take_card(order_of_hands[i])
        self.predict_players()
    
    def show_game(self):
        self.players = []
        for i in range(len(self.game.players)):
            self.players.append([{self.game.players[i].name : self.game.players[i].cards}, 
                                 self.game.players[i].pairs, self.game.players[i].amount_points])
        return self.players
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


class Statistics:
    pass
