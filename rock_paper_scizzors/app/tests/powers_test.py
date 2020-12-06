import unittest
from app.models.powers import *
from app.models.power import Power

class TestPowers(unittest.TestCase):

    def setUp(self):
        self.rock = Power("Rock")
        self.paper = Power("Paper")
        self.scizzors = Power("Scizzors")

    def test_rock_beats_scizzors(self):
        self.assertEqual(self.rock, winning_power(self.rock, self.scizzors))

    def test_scizzors_not_beat_rock(self):
        self.assertEqual(self.rock, winning_power(self.scizzors, self.rock))

    def test_scizzors_beat_paper(self):
        self.assertEqual(self.scizzors, winning_power(self.scizzors, self.paper))

    def test_paper_not_beat_scizzors(self):
        self.assertEqual(self.scizzors, winning_power(self.paper, self.scizzors))


    def test_paper_beats_rock(self):
        self.assertEqual(self.paper, winning_power(self.paper, self.rock))

