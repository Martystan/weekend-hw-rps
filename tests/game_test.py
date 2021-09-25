import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("player1", "rock")
        self.player2 = Player("player2", "scissors")
        

    def test_if_rock_beats_scissors(self):
        result = Game.who_wins(self)
        self.assertEqual(self.player1, result )

