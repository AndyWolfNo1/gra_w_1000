from flask import Flask
from config import Config
from flask import render_template
from flask import request
from flask import jsonify
from random import shuffle
import jinja2
from tysiac import *
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)
env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 
app_name = "Gra w 1000"

names = ['Marek', 'Stefan', 'Janusz', 'Bogdan']
players = [Player(name) for name in names]
game = Game()

@app.route('/',methods = ['POST', 'GET'])
def start_panel():
    return render_template('start_panel.html')

@app.route('/game',methods = ['POST', 'GET'])
def start():
    if request.method == 'POST':
        form_data = request.form
        if form_data['name'] == '/musik':
            game.step1()
            adress = '/gra'
            n_a = 'Rozdaj musik'
            return render_template('start.html', adress=adress, n_a=n_a)
        if form_data['name'] == '/gra':
            game.step2()
            if game.error == True:
                return render_template('error.html')
            if game.error == False:
                adress = '/first_move'
                n_a = 'Licytacja'
                return render_template('start.html', adress=adress, n_a=n_a)
        if form_data['name'] == '/first_move':
            game.game_raport()
            if game.moves == 7:
                game.moves = 0
            game.step3()
            if game.moves < 6:
                n_a = 'Graj'
            if game.moves == 6:
                n_a = "Dalej"
            adress = '/first_move'
            script = f"<script>my_f();</script>"
            return render_template('start.html', adress=adress, n_a=n_a, script=script)
    game.moves = 0
    game.licit_val = 0
    game.deal_the_cards(players)
    game.auction()
    game.test_cards = None
    adress = '/musik'
    n_a = 'Daj musik'
    information = "Licytację wygrywa gracz {}, zabierz musik i rozpocznij grę.".format(game.players[game.max_auction_id[0]])
    return render_template('start.html', adress=adress, n_a=n_a, info=information)

@app.route('/licit',methods = ['POST', 'GET'])
def licit():
    adress = '/first_move'
    n_a = 'Zacznij grę'
    if request.method == 'POST':
            f_d = request.form
            licit = f_d['licit']
            if licit != '':
                game.licit_val = int(licit)
            else:
                game.licit_val = 100
            return render_template('start.html', adress=adress, n_a=n_a)
    
@app.route('/test',methods = ['POST', 'GET'])
def data():
    df = pd.read_csv('test.csv')
    return render_template('test2.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/process', methods=['POST'])
def process():
    json_data = request.get_json()
    input_data = json_data['input']
    output_data = input_data.upper()
    #return jsonify(output=output_data)
    return jsonify(output=['output_data', 'cos'])

@app.context_processor
def inject_variables():
    return dict(
        app_name=app_name,
        game= game
        )


if __name__ =='__main__':
    app.run(debug=True)