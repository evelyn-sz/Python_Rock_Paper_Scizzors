import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game_1 = Game("Rich", "Scott")
        self.game_1 = Game("Scott", "Paul")
        self.game_1 = Game("Paul", "Rich")
        self.player_1 = Player("Rich", "Rock")
        self.player_2 = Player("Paul", "Paper")
        self.player_3 = Player("Scott", "Scizzors")


    def test_rock_beats_scizzors(self):
        self.assertEqual(self.player_1.name, self.game_1.winning_power(self.player_1, self.player_3))

    def test_scizzors_not_beat_rock(self):
        self.assertEqual(self.player_1.name, self.game_1.winning_power(self.player_3, self.player_1))

    def test_scizzors_beat_paper(self):
        self.assertEqual(self.player_3.name, self.game_1.winning_power(self.player_3, self.player_2))

    def test_paper_not_beat_scizzors(self):
        self.assertEqual(self.player_3.name, self.game_1.winning_power(self.player_2, self.player_3))

    def test_paper_beats_rock(self):
        self.assertEqual(self.player_2.name, self.game_1.winning_power(self.player_2, self.player_1))

    def test_rock_not_beat_paper(self):
        self.assertEqual(self.player_2.name, self.game_1.winning_power(self.player_1, self.player_2))

