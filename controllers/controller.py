from flask import render_template, request
from app import app
from models.game import *
from models.player import *

@app.route('/')
def home_route():
    return render_template('base.html')

@app.route('/play')
def play_route():
    return render_template('play.html')

@app.route('/multiplayer')
def multiplayer_route():
    return render_template('multiplayer.html')

@app.route('/welcome')
def welcome_route():
    return render_template('welcome.html')

@app.route('/<choice1>/<choice2>')
def show_results(choice1, choice2):
    victory=simple_game(choice1, choice2)
    if victory == None:
        return render_template('winner.html', winner="nobody", winning_move="a draw")
    return render_template('winner.html', winner=victory.player_number, winning_move=victory.choice)

@app.route('/play', methods=['POST'])
def make_results():
    player_number=request.form['name']
    choice=request.form['choice']
    new_player=Player(player_number,choice)
    computer=make_computer()
    victory=run_game(new_player, computer)
    if victory == None:
        return render_template('winner.html', winner="nobody", winning_move="a draw")
    return render_template('winner.html', winner=victory.player_number, winning_move=victory.choice)

@app.route('/multiplayer', methods=['POST'])
def make_multiplayer_results():
    player_number=request.form['name']
    choice=request.form['choice']
    new_player=Player(player_number,choice)
    player_number=request.form['name2']
    choice=request.form['choice2']
    new_player2=Player(player_number,choice)
    victory=run_game(new_player, new_player2)
    if victory == None:
        return render_template('winner.html', winner="nobody", winning_move="a draw")
    return render_template('winner.html', winner=victory.player_number, winning_move=victory.choice)
