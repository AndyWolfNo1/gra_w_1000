from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
from flask import session
from random import shuffle
import jinja2
from tysiac import *
import json
import sqlite3


app = Flask(__name__)
app.secret_key = b'fafafiansonoqifn;lkadav'

env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 
app_name = "Gra w 1000"
table = Table()
names = ['Marek', 'Stefan', 'Janusz']
players = [Player(name) for name in names]


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def start_panel():
    if 'logged_in' in session:
        return render_template('start_panel.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/table',methods = ['POST', 'GET'])
def table_panel():
    if 'logged_in' in session:
        return render_template('table.html', username=session['username'])
    else:
        return redirect(url_for('login'))
    

@app.route('/game/<int:id_game>')
def show_game(id_game):
    if 'logged_in' in session:
        game = table.return_game_by_id(id_game)
        return render_template('show_game.html', game=game, username=session['username'])
    else:
        return redirect(url_for('login'))
    

@app.route('/process', methods=['POST','GET'])
def process():
    json_data = request.get_json()
    process = int(json_data['process'])
    if process == 0:
        player = json_data['player']
        player = Player(player)
        id_game = json_data['id']
        table.add_player_to_game(int(id_game), player)
        print('dodano gracza {} do gry {}'.format(player.name, id_game))
        res = table.return_json_players(int(id_game))
        print("process 0")
        return res
    if process == 1:
        id_game = json_data['id']
        res = table.return_json_players(int(id_game))
        print('process1')
        return res
    if process == 2:
        creator_name = json_data['name']
        game = Game()
        table.add_game(game, creator_name)
        print('process2')
        data = {
            "id": game.ID,
            "creator" : creator_name,
            "start_time": game.string_start_time
                }
        return json.dumps(data)
    if process == 3:
        table.check_old_games()
        res = table.return_game_to_table()
        print('process3')
        return json.dumps(res)
    # if process == 4:
    #     user.change_name(json_data['username'])
    #     print("process4")
    #     return user.name
    if process == 5:
        json_data = request.get_json()
        id_game = json_data['id']
        table.activate_game_by_id(id_game)
        print('process5')
        return "success"
  
@app.route('/activate', methods=['GET'])
def get_objects():
    active_games = table.return_active_games()
    print('activate')
    return jsonify(active_games)
      
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='Hasła nie są takie same.')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()

        if user is not None:
            session['logged_in'] = True
            session['username'] = user['username']
            return redirect(url_for('table_panel'))
        else:
            error = 'Nieprawidłowa nazwa użytkownika lub hasło.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('start_panel'))

@app.context_processor
def inject_variables():
    return dict(
        app_name=app_name,
        table=table
        )

if __name__ =='__main__':
    app.run(debug=True)