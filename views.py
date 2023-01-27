from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from random import shuffle
import jinja2
from tysiac import *
import pandas as pd

app = Flask(__name__)
env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 
app_name = "Gra w 1000"

names = ['Marek', 'Stefan', 'Janusz', 'Bogdan']
players = [Player(name) for name in names]
game = Game()


@app.route('/',methods = ['POST', 'GET'])
def start():
    game.deal_the_cards(players)
    game.auction()
    return render_template('start.html')

@app.route('/musik',methods = ['POST', 'GET'])
def take_musik():
    game.step1()
    button = 1
    return render_template('start.html', button=button)

@app.route('/gra',methods = ['POST', 'GET'])
def start_game():
    game.step2()
    button = 0
    return render_template('start.html', button=button)

@app.route('/first_move',methods = ['POST', 'GET'])
def first_move():
    return render_template('first_move.html')
    
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


app.run(debug=True)