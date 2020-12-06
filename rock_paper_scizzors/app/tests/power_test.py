import unittest
from app.models.power import Power

class TestPower(unittest.TestCase):

    def setUp(self):
        self.power_1 = Power("Rock")
        self.power_2 = Power("Paper")
        self.power_3 = Power("Scizzors")

    def test_power_has_name(self):
        self.assertEqual("Rock", self.power_1.name)
