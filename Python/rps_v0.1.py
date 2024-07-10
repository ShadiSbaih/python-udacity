import random

class Player:
    def __init__(self):
        self.my_move = 'rock'

    def learn(self, my_move, their_move):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        elif self.my_move == 'scissors':
            self.my_move = 'lizard'
        elif self.my_move == 'lizard':
            self.my_move = 'spock'
        else:
            self.my_move = 'rock'

class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

class SequentialPlayer(Player):
    def __init__(self):
        self.index = 0
        self.moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.my_move = self.moves[self.index]

    def learn(self, my_move, their_move):
        self.my_move = self.moves[self.index]
        self.index = (self.index + 1) % 5

class StaticPlayer(Player):
    def __init__(self, move):
        self.my_move = move

def beats(one, two):
    return ((one == 'scissors' and two in ['paper', 'lizard']) or
            (one == 'paper' and two in ['rock', 'spock']) or
            (one == 'rock' and two in ['lizard', 'scissors']) or
            (one == 'lizard' and two in ['spock', 'paper']) or
            (one == 'spock' and two in ['scissors', 'rock']))

class Colors:
    ROCK = '\033[91m'
    PAPER = '\033[92m'
    SCISSORS = '\033[93m'
    LIZARD = '\033[94m'
    SPOCK = '\033[95m'
    END = '\033[0m'

def colorize(move):
    if move == 'rock':
        return Colors.ROCK + move + Colors.END
    elif move == 'paper':
        return Colors.PAPER + move + Colors.END
    elif move == 'scissors':
        return Colors.SCISSORS + move + Colors.END
    elif move == 'lizard':
        return Colors.LIZARD + move + Colors.END
    elif move == 'spock':
        return Colors.SPOCK + move + Colors.END

def play_round(player1, player2):
    move1 = colorize(player1.my_move)
    move2 = colorize(player2.my_move)
    print(f"Player 1: {move1}  Player 2: {move2}")
    if beats(player1.my_move, player2.my_move):
        print("Player 1 wins!")
    elif beats(player2.my_move, player1.my_move):
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    player1.learn(player1.my_move, player2.my_move)
    player2.learn(player2.my_move, player1.my_move)

def tournament(players):
    scores = {player.__class__.__name__: 0 for player in players}
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            player1 = players[i]
            player2 = players[j]
            print(f"===== Match: {type(player1).__name__} vs {type(player2).__name__} =====")
            for _ in range(5):  # Play 5 rounds
                play_round(player1, player2)
                if beats(player1.my_move, player2.my_move):
                    scores[type(player1).__name__] += 1
                elif beats(player2.my_move, player1.my_move):
                    scores[type(player2).__name__] += 1
            print()
    print("===== Tournament Results =====")
    for player, score in scores.items():
        print(f"{player}: {score}")

# Example usage
if __name__ == "__main__":
    players = [
        Player(),
        RandomPlayer(),
        SequentialPlayer(),
        StaticPlayer('rock'),
        StaticPlayer('spock')
    ]
    tournament(players)
