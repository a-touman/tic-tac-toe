import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_start_game(self):
        game = Game()
        game.start_game()

    def test_make_move(self):
        game = Game()
        board = game.board
        self.assertEqual(board.make_move('X', 0, 0), True)

if __name__ == '__main__':
    unittest.main()