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
game.licit_val = 0

@app.route('/',methods = ['POST', 'GET'])
def start():
    game.check_in = [0,0,0,0]
    if request.method == 'POST':
        form_data = request.form
        if form_data['name'] == '/musik':
            game.step1()
            adress = '/gra'
            n_a = 'Rozdaj musik'
            return render_template('start.html', adress=adress, n_a=n_a)
        if form_data['name'] == '/gra':
            game.step2()
            adress = '/first_move'
            n_a = 'Licytacja'
            return render_template('start.html', adress=adress, n_a=n_a)
        if form_data['name'] == '/first_move':
            game.step3()
            n_a = 'n_step'
            adress = '/first_move'
            script = f"<script>my_f();</script>"
            return render_template('start.html', adress=adress, n_a=n_a, script=script)
    game.licit_val = 0
    game.deal_the_cards(players)
    game.auction()
    game.test_cards = None
    adress = '/musik'
    n_a = 'Daj musik'
    return render_template('start.html', adress=adress, n_a=n_a)

@app.route('/licit',methods = ['POST', 'GET'])
def licit():
    adress = '/first_move'
    n_a = 'Zacznij grę'
    if request.method == 'POST':
            f_d = request.form
            game.licit_val = f_d['licit']
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