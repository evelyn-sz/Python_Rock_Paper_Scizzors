import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Rich", "Rock")
        self.player_2 = Player("Paul", "Paper")
        self.player_3 = Player("Scott", "Scizzors")

    
    def test_player_has_name(self):
        self.assertEqual("Rich", self.player_1.name)
        self.assertEqual("Paul", self.player_2.name)
        self.assertEqual("Scott", self.player_3.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player_1.choice)
        self.assertEqual("Paper", self.player_2.choice)
        self.assertEqual("Scizzors", self.player_3.choice)