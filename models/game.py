from models.player import Player

class Game:
    def __init__(self, choice1, choice2):
        self.choice1 = choice1
        self.choice2 = choice2

def run_game(player1, player2):
    if player1.choice == player2.choice:
        return None
    elif player1.choice == "rock" and player2.choice == "paper":
        return player2
    elif player1.choice == "paper" and player2.choice == "scissors":
        return player2
    elif player1.choice == "scissors" and player2.choice == "rock":
        return player2
    return player1
    