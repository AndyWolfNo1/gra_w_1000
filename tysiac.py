import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


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
        self.master_color = None
        self.remove_cards = []
        self.win_points = 0
        self.match_points = 0
        
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

    def create_array_colors(self):
        self.array_colors = np.zeros(4)
        reshape_cards = self.array_cards.reshape(4,6)
        for i in range(4):
            if reshape_cards[i][2] == 1 and reshape_cards[i][3] == 1:
                self.array_colors[i] = 1
        
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
        if len(res)>3:
            res.pop()
        if len(res)<3:
            res.append(cards[-1].id)
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
        
    def start_move(self):
        self.master = [0,0,0,0]
        colors = self.create_colors()
        #colors = ['trefl','pik','kier','karo']
        cards = self.cards
        for i in range(len(cards)):
            if cards[i].name=='A':
                self.remove_cards.append(cards[i])
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name == '10':
                for j in range(len(self.remove_cards)):
                    if self.remove_cards[j].name == "A" and cards[i].color == self.remove_cards[j].color:
                        res = self.return_cards_by_id([cards[i].id])
                        return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name=='Q':
                self.master_color = cards[i].color
                if self.master_color == 'trefl':
                    self.match_points += 100
                    self.master = [1,0,0,0]
                if self.master_color == 'pik':
                    self.match_points += 80
                    self.master = [0,1,0,0]
                if self.master_color == 'kier':
                    self.match_points += 60
                    self.master = [0,0,1,0]
                if self.master_color == 'karo':
                    self.match_points += 40
                    self.master = [0,0,0,1]
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name=='10' and self.master_color == cards[i].color :
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name=='K':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name=='J':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].color in colors and cards[i].name=='9':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].name=='10':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].name=='K':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].name=='Q':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].name=='J':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
        for i in range(len(cards)):
            if cards[i].name=='9':
                res = self.return_cards_by_id([cards[i].id])
                return res[0]
            
    def play(self, data):
        start_card = data[0]
        check_in = data[1]
        for i, j in enumerate(self.colors):
            if check_in[i] == 1:
                check_in = j
                break
            if i == 3 and isinstance(check_in, list):
                check_in = 0
        if check_in != 0 and isinstance(check_in, str):
            try:
                cards_from_color = list(filter(lambda x: x.color == check_in, self.cards))
                highest_card = max(cards_from_color, key=lambda x: x.value)
                if highest_card:
                    return highest_card
            except:
                try:
                    cards_from_color = list(filter(lambda x: x.color == check_in, self.cards))
                    lowest_card = min(cards_from_color, key=lambda x: x.value)
                    if lowest_card:
                        return lowest_card
                except:
                    try:
                        lowest_card = min(self.cards, key=lambda x: x.value)
                        return lowest_card
                    except:
                        pass
        if check_in == 0:
            try:
                cards_from_color = list(filter(lambda x: x.color == start_card.color, self.cards))
                lowest_card = min(cards_from_color, key=lambda x: x.value)
                if lowest_card:
                    return lowest_card
            except:
                pass
        if check_in == 0 :
            try:
                lowest_card = min(self.cards, key=lambda x: x.value)
                return lowest_card
            except:
                pass

    def add_match_points(self, points):
        self.match_points += points
    
    def add_win_points(self, points):
        self.win_points += points
        
            
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
        self.moves = 0
        self.players = []
        self.start_card = None
        self.licit_val = 0
        self.licit_val = 100
        self.statistics = Statistics()
        self.g_r = "brak"
        
    def suffle_cards(self):
        self.new_cards = Deck().take()
        shuffled_cards = []
        while len(self.new_cards) > 0:
            index = random.randint(0, len(self.new_cards) - 1)
            shuffled_cards.append(self.new_cards[index])
            self.new_cards.pop(index)
        return shuffled_cards

    def deal_the_cards(self, players):
        self.start_card = False
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
            self.players[i].create_array_colors()
            self.players[i].gen_auction()
        #self.check_in = 0
        
    def auction(self):
        self.auction_res = dict()
        for i in range(4):
            self.auction_res[self.players[i].ID] = self.players[i].auction
        maximum = max([x for x in self.auction_res.values()])
        self.max_auction_id = [key for key, value in self.auction_res.items() if value == maximum]
        self.check_in = [0,0,0,0]

    def o_o_p(self, start_id):
        '''Order of players '''
        if start_id == 0:
            return [1,2,3]
        if start_id == 1:
            return [2,3,0]
        if start_id == 2:
            return [3,0,1]
        if start_id == 3:
            return[0,1,2]
        
    def game_raport(self):
        licit =self.licit_val
        match_points = self.master_player.match_points
        if licit <= match_points:
            result = 'udało się ugrać' 
        else:
            result = 'nie udało się ugrać'
        self.g_r = '''Grę wylicytował {}. Licytacja {}.
        Gracz ugrał {}.
        Graczowi {}
        '''.format(self.master_player, self.licit_val, self.master_player.match_points, result)
        
    def move(self, start_id):
        start_card = self.players[start_id].start_move()
        if sum(self.players[self.max_auction_id[0]].master)>0:
            self.check_in = self.players[self.max_auction_id[0]].master
        o_o_p = self.o_o_p(self.max_auction_id[0])
        self.play_cards = [None,None,None,None]
        for i in range(4):
            if self.max_auction_id[0] == i:
                self.play_cards[i] = start_card
        
        for i in o_o_p:
            card = self.players[i].play([start_card, self.check_in])
            try:
                self.players[i].return_cards_by_id([card.id])
            except:
                pass
            self.play_cards[i] = card
        self.moves += 1

    def step1(self):
        self.error = False
        self.moves = 0
        self.play_cards = []
        self.auction()
        self.master_player = None
        if len(self.max_auction_id)==1:
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()
            for i in range(4):
                self.players[i].create_cards_array()
                self.players[i].gen_auction()
                self.players[i].match_points = 0
                self.players[i].create_array_colors()
        else:
            #do poprawy
            self.players[self.max_auction_id[0]].take_card(self.musik, musik=True)
            self.players[self.max_auction_id[0]].sorted_cards()
            for i in range(4):
                self.players[i].create_cards_array()
                self.players[i].gen_auction()
                self.players[i].create_array_colors()
        self.musik = []

    def step2(self):
        try:
            all_id = [0,1,2,3]
            self.return_musik = self.players[self.max_auction_id[0]].take_3_min_cards()
            self.return_musik2 = self.players[self.max_auction_id[0]].return_cards_by_id(self.return_musik)
            win_player_id = self.max_auction_id[0]
            del all_id[win_player_id]
            for i, n in enumerate(all_id):
                self.players[n].take_one_card(self.return_musik2[i])
            self.master_player = self.players[self.max_auction_id[0]]
            for i in range(4):
                self.players[i].gen_auction()
                self.players[i].create_array_colors()
        except:
            self.error = True

    def step3(self):
        try:
            self.move(self.max_auction_id[0])
            if self.check_in[0] == 1:
                color = 'trefl'
            if self.check_in[1] == 1:
                color = 'pik'
            if self.check_in[2] == 1:
                color = 'kier'
            if self.check_in[3] == 1:
                color = 'karo'
            if sum(self.check_in)==0:
                color = None
            self.gameplay_result = [self.play_cards, self.max_auction_id[0], color]
            self.statistics.add_game(self)
            self.statistics.check_the_gameplay()
        except:
            self.error = True
        

class Statistics:
    def __init__(self):
        pass
     
    def add_game(self, game):
        self.game = game
    
    def check_the_gameplay(self):
        if self.game:
            if self.game.moves < 7:
                gameplay_result = self.game.gameplay_result
                max_card = gameplay_result[0][gameplay_result[1]]
                max_id = gameplay_result[1]
                res = 0
                if gameplay_result[2] != None:
                    if max_card.color == gameplay_result[2]:
                        for i, j in enumerate(gameplay_result[0]):
                            if j.color ==  gameplay_result[2] and j.value > max_card.value:
                                max_card = j
                                max_id = i
                    if max_card.color != gameplay_result[2]:
                        for i, j in enumerate(gameplay_result[0]):
                            value = 0
                            if j.color == gameplay_result[2] and j.value > value:
                                max_card = j
                                max_id = i
                                value += j.value
                                res = 1
                        if res == 0:
                            for i, j in enumerate(gameplay_result[0]):
                                if j.value > max_card.value:
                                    max_card = j
                                    max_id = i  
                else:
                    for i, j in enumerate(gameplay_result[0]):
                        if j.value > max_card.value:
                            max_card = j
                            max_id = i
                            print("else")
                points = sum(card.value for card in gameplay_result[0]) 
                self.game.players[max_id].add_match_points(points)
                self.game.max_auction_id[0] = max_id
                if self.game.moves == 6:
                    self.add_points()
                return max_card, max_id

    def add_points(self):
        master_player = self.game.master_player
        licit = self.game.licit_val
        if licit > master_player.match_points:
            res = -(licit)
            self.game.master_player.add_win_points(res)
        if licit < master_player.match_points:
            res = round(master_player.match_points, -1)
            self.game.master_player.add_win_points(res)   
            
        
                
        
    
    
    
    
    
    
    
    
    
    
    