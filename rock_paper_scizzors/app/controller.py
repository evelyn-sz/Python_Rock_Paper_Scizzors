from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/rock', methods=['POST'])
# def play_game():
#     player_1 = request.form['name']
#     player_2 = request.form['name']
#     game_played = Game(player_1=player_1, player_2=player_2)
#     winning_power(player_1, player_2)
#     return redirect('/')