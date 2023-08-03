from vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 10)
