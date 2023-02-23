import random
import numpy as np
import datetime
import time
import json


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

    def __str__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu w obiekcie print()"""
        return self.name+' '+self.color

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
        self.name = name
        self.ID = int()
        
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
   
    def take_cards(self, cards, musik = None):
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

    def add_match_points(self, points):
        self.match_points += points
    
    def add_win_points(self, points):
        self.win_points += points


class Game:
    title ="A_trefl,10_trefl,K_trefl,D_trefl,J_trefl,9_trefl,A_pik,10_pik,K_pik,D_pik,J_pik,9_pik,A_kier,10_kier,K_kier,D_kier,J_kier,9_kier,A_karo,10_karo,K_karo,D_karo,J_karo,9_karo,trefl,pik,kier,karo\n"
    index = title.split(',')
    indexs = index[:-4]
    
    def __init__(self):
        self.start_time = time.time()
        current_time = datetime.datetime.now()
        self.string_start_time = current_time.strftime("%H:%M:%S")
        self.ID = self.gen_game_id()
        self.players = []
        strtime = str(self.ID)
        self.id = strtime[-4:]
        self.json_players()
        self.len_players = 0
        self.creator = ''
        self.activate = 0
        
    def add_player(self, player):
        self.players.append(player)
        self.json_players()
        self.remove_duplicates_players()
        
    def json_players(self):
        if len(self.players) == 0:
            data = {0 : "brak"}
            self.jsplayers = json.dumps(data)
        else:
            data= dict() 
            for i in range(len(self.players)):
                data[i] = self.players[i].name
                self.jsplayers = json.dumps(data)

    def __repr__(self):
        strtime = str(self.ID)
        return "Gra id: {} utworzona {}".format(strtime[-4:], self.string_start_time)

    def gen_game_id(self):
        current_time = datetime.datetime.now()
        ft = current_time.strftime("%Y%m%d%H%M%S")
        ft += str(random.randint(0, 9))
        ft += str(random.randint(0, 9))
        return int(ft)
        
    def remove_duplicates_players(self):
        unique_players = []
        names = []
        for player in self.players:
            if player.name not in names:
                names.append(player.name)
                unique_players.append(player)
        self.len_players = len(unique_players)
        self.players = unique_players


class Table:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.games = []
        self.deleted_games = []
        
    def add_game(self, game, name):
        game.creator = name
        for i in range(len(self.games)):
            self.check_old_games()
        self.games.append(game)
    
    def del_game_by_id(self, game_id):
        for i in range(len(self.games)):
            if self.games[i].ID == game_id:
                del self.games[i]
                break
       
    def check_old_games(self):
        current_time = time.time()
        for i in range(len(self.games)):
            time_difference = abs(self.games[i].start_time - current_time)
            if time_difference >= 60 and len(self.games[i].players) == 0 :
                self.deleted_games.append(self.games[i])
                del self.games[i]
                break

    def add_player_to_game(self, id_game, player):
        for i in range(len(self.games)):
            if self.games[i].ID == id_game:
                self.games[i].add_player(player)
            self.games[i].remove_duplicates_players()
            
    def return_json_players(self, id_game):
        for i in range(len(self.games)):
            if self.games[i].ID == id_game:
                self.games[i].json_players()
                return self.games[i].jsplayers

    def return_game_to_table(self):
        res = dict()
        for i in range(len(self.games)):
            res[i] = {
                    "id" : self.games[i].ID,
                    "creator" : self.games[i].creator,
                    "len_players" : self.games[i].len_players,
                    "start_time": self.games[i].string_start_time,
                    "activate" : self.games[i].activate}
        return res
    
    def activate_game_by_id(self, id_game):
        for i in range(len(self.games)):
            if self.games[i].ID == id_game:
                self.games[i].activate = 1
                
    def return_active_games(self):
        res = []
        data = dict()
        for i in range(len(self.games)):
            if self.games[i].activate == 1:
                res.append(self.games[i].ID)
        if len(res)>0:
            for i in range(len(res)):
                data[i] = res[i]
        return data
    
    def return_game_by_id(self, id_game):
        for i in range(len(self.games)):
            if self.games[i].ID == id_game:
                return self.games[i]
   
        
    
    
    
    
    
    
    
    
    