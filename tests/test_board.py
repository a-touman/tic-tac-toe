import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def test_print_board(self):
        board = Board()
        board.print_board()

    def test_make_move(self):
        board = Board()
        self.assertEqual(board.make_move('X', 0, 0), True)

if __name__ == '__main__':
    unittest.main()