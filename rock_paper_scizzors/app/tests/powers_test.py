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