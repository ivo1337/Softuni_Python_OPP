class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def __str__(self):
        return f'The point has coordinates ({self.x},{self.y})'


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        p = Point(20, 40)
        self.assertEqual(p.x, 20)
        self.assertEqual(p.y, 40)

    def test_set_x(self):
        p = Point(10, 20)
        p.set_x(7)
        self.assertEqual(p.x, 7)

    def test_set_y(self):
        p = Point(10, 20)
        p.set_y(18)
        self.assertEqual(p.y, 18)

    def test_distance(self):
        p = Point(10, 11)
        res = p.__str__()
        self.assertEqual(res, 'The point has coordinates (10,11)')


if __name__ == "__main__":
    unittest.main()