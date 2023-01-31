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
        self.last_move = [None, None]
        
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
        
    def create_colors(self):
        res = []
        if self.array_colors[0] > 0:
            res.append('trefl')
        if self.array_colors[1] > 0:
            res.append('pik')
        if self.array_colors[2] > 0:
            res.append('kier')
        if self.array_colors[3] > 0:
            res.append('karo')
        self.colors_name = res
        return res
   
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
        self.reshape_cards = self.array_cards.reshape(4,6)
        for i in range(4):
            buff.append(list(self.reshape_cards[i]))
        for i in range(4):
            #redukcja dziewiątek
            buff[i][5] = 0.
            buff[i][4] = 0.
            #dodawanie wartoci koloru
            buff[i].append(self.array_colors[i])
            suma += sum(buff[i])*c
            c -= 0.20
        self.auction = round(suma, 3)+sum(self.array_colors)
        
    def take_3_min_cards(self):
        cards = self.cards
        n_colors = ['trefl','pik','kier','karo']
        colors = []
        res = []
        
        for i in range(4):
            if self.array_colors[i]==1:
                colors.append(n_colors[i])
        
        while len(res)<3:
            for i in range(len(cards)):
                if cards[i].name =='9':
                    res.append(cards[i].id)
            for i in range(len(cards)):
                if cards[i].name =='J' and cards[i].color not in colors and len(res)<3:
                    res.append(cards[i].id)
            for i in range(len(cards)):
                if cards[i].name =='Q' and cards[i].color not in colors and len(res)<3:
                    res.append(cards[i].id)
            for i in range(len(cards)):
                if cards[i].name =='K' and cards[i].color not in colors and len(res)<3:
                    res.append(cards[i].id)
            for i in range(len(cards)):
                if cards[i].name =='10' and cards[i].color not in colors and len(res)<3:
                    res.append(cards[i].id)
            for i in range(len(cards)):
                if cards[i].name =='A' and cards[i].color not in colors and len(res)<3:
                    res.append(cards[i].id)
        if len(res)<3:
            res.pop()
        return res
    
    def take_one_card(self, card):
        self.cards.append(card)
        self.sorted_cards()
        self.create_cards_array()
    
    def return_cards_by_id(self, card_id:list):
        i_d = len(card_id)
        res = []
        iters = 0
                
        while iters <= i_d:
            for i in range(len(self.cards)):
                if self.cards[i].id in card_id:
                    res.append(self.cards[i])
                    del self.cards[i]
                    break
            iters += 1
        return res      
    
    def change_check_in(self, mode):
        self.check_in = mode
        
    def move(self):
        self.create_colors()
        if self.last_move[0] == None:        
            for i in range(len(self.cards)):
                if self.cards[i].name == 'A':
                    if self.cards[i].color in self.colors_name:
                        res = self.return_cards_by_id([self.cards[i].id])
                        self.last.move[0] = self.cards[i].name
                        self.last_move[1] = self.cards[i].color
                        break
                    else:
                        res = self.return_cards_by_id([self.cards[i].id])
                        self.last.move[0] = self.cards[i].name
                        break
        if self.last_move[0] != None and self.last_move[1] == None:
            if self.last_move[0] == 'A':
                pass
                
            
        return res
                    
            
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
        self.master_player = None
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
        self.musik.append(self.s_cards[5::6])
        self.musik = sorted(self.musik[0], key=lambda card: card.id, reverse=False)
        
        for i in range(4):
            self.players[i].take_card(order_of_hands[i])
            self.players[i].ID = i
        self.predict_players()
        self.check_in = 0
    
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
        self.auction_res = dict()
        for i in range(4):
            self.auction_res[self.players[i].ID] = self.players[i].auction
        maximum = max([x for x in self.auction_res.values()])
        self.max_auction_id = [key for key, value in self.auction_res.items() if value == maximum]

    def change_check_in(self, mode):
        for i in range(len(self.players)):
            self.players[i].change_check_in(mode)
            self.check_in = mode

    def step1(self):
        self.check_in = 0
        self.auction()
        self.master_player = None
        if len(self.max_auction_id)==1:
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()
            for i in range(4):
                self.players[i].create_cards_array()
                self.players[i].gen_auction()
            self.predict_players()
        else:
            #do poprawy
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()
            for i in range(4):
                self.players[i].create_cards_array()
                self.players[i].gen_auction()
            self.predict_players()
        self.musik = []

    def step2(self):
        all_id = [0,1,2,3]
        self.return_musik = self.players[self.max_auction_id[0]].take_3_min_cards()
        self.return_musik2 = self.players[self.max_auction_id[0]].return_cards_by_id(self.return_musik)
        win_player_id = self.max_auction_id[0]
        del all_id[win_player_id]
        for i, n in enumerate(all_id):
            self.players[n].take_one_card(self.return_musik2[i])
        self.master_player = self.players[self.max_auction_id[0]]
        self.predict_players()
        for i in range(4):
            self.players[i].gen_auction()

    def step3(self):
        #self.change_check_in([1,0,0,0])
        pass










