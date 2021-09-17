from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/')
def home_route():
    return render_template('index.html')

@app.route('/welcome')
def welcome_route():
    return render_template('welcome.html')

@app.route('/<choice1>/<choice2>')
def show_results(choice1, choice2):
    victory=simple_game(choice1, choice2)
    if victory == None:
        return render_template('winner.html', winner="nobody", winning_move="a draw")
    return render_template('winner.html', winner=victory[0], winning_move=victory[1])
