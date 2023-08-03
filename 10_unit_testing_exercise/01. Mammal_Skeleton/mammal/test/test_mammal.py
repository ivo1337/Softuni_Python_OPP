from project.mammal import Mammal
import unittest

class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "TestType", "TestSound")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Test")
        self.assertEqual(self.mammal.type, "TestType")
        self.assertEqual(self.mammal.sound, "TestSound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Test makes TestSound")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Test is of type TestType")