import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_get_symbol(self):
        player = Player('X')
        self.assertEqual(player.get_symbol(), 'X')

if __name__ == '__main__':
    unittest.main()