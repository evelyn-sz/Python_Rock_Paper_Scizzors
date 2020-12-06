import unittest
from app.models.power import Power

class TestPower(unittest.TestCase):

    def setUp(self):
        self.rock = Power("Rock")
        self.paper = Power("Paper")
        self.scizzors = Power("Scizzors")

    def test_power_has_name(self):
        self.assertEqual("Rock", self.rock.name)
        self.assertEqual("Paper", self.paper.name)
        self.assertEqual("Scizzors", self.scizzors.name)
