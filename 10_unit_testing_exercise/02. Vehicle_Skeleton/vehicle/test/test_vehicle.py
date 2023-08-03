from project.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 10)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(10, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.assertEqual(97.5, self.vehicle.fuel)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.assertEqual("The vehicle has 10 horse power with 100 fuel left and 1.25 fuel consumption", str(self.vehicle))