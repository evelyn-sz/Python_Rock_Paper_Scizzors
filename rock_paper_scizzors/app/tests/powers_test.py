import unittest
from app.models.powers import *
from app.models.power import Power

class TestPower(unittest.TestCase):

    def setUp(self):
        self.rock = Power("Rock")
        self.paper = Power("Paper")
        self.scizzors = Power("Scizzors")

    