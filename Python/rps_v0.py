import random

# Possible moves in the game
moves = ['rock', 'paper', 'scissors']


# Base player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Function to determine if one move beats another
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Player that chooses moves randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Player that takes input from a human
class HumanPlayer(Player):
    def move(self):
        move = input("Enter your move (rock, paper, or scissors): ").lower()
        while move not in moves:
            move = input("Please enter rock, paper, or scissors: ").lower()
        return move


# Player that repeats the opponent's last move
class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


# Player that cycles through the moves
class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        elif self.my_move == 'scissors':
            self.my_move = 'rock'


# Player that always chooses rock
class RockPlayer(Player):
    def move(self):
        return 'rock'


# Class to represent the game
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    # Play a single round of the game
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins the round!")
            self.p2_score += 1
        else:
            print("It's a tie!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Play a game consisting of 3 rounds
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
            print(f"Score: Player 1: {self.p1_score}, Player 2: {self.p2_score}")
        print("Game over!")
        print(f"Final score: Player 1: {self.p1_score}, Player 2: {self.p2_score}")


if __name__ == "__main__":
    # Create a game with a human player and a reflecting player
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
