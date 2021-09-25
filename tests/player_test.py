import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("player1", "rock")
        self.player2 = Player("player2", "scissors")

    def test_player_has_id(self):
        self.assertEqual("player1", self.player1.id)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player1.choice)