from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')

    def start_game(self):
        current_player = self.player1
        while True:
            self.board.print_board()
            move = input(f"Player {current_player.symbol}, enter your move (row and column numbers, e.g. 0-0): ")
            row, col = [int(x) for x in move.split('-')]
            if self.board.make_move(current_player.symbol, row, col):
                current_player = self.player2 if current_player == self.player1 else self.player1
                if self.board.has_won():
                    print(f"Player {current_player.symbol} wins!")
                    break
            else:
                print("Invalid move. Try again!")

    def play(self):
        while True:
            self.start_game()