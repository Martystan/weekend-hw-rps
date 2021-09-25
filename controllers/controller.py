from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def index():
    return render_template ('home.html', title = 'RPS')

@app.route('/game', methods= ['GET' , 'POST'])
def pick_your_weapon():
    weapons = ["rock", "paper", "scissors"]

    data_Player1 = request.form.get('Player 1')
    data_Player2 = request.form.get('Player 2')
    player1 = Player("Tom", data_Player1)
    player2 = Player("Jerry", data_Player2)

    game = Game(player1, player2)

    result = game.who_wins()

    
    
    return render_template ('game.html' , weapons = weapons, result = result)
    


