from unittest import TestCase

class Worker:
  def __init__(self, name, salary, energy):
    self.name = name
    self.salary = salary
    self.energy = energy
    self.money = 0

  def work(self):
    if self.energy <= 0:
        raise Exception('Not enough energy.')

    self.money += self.salary
    self.energy -= 1

  def rest(self):
    self.energy += 1

  def get_info(self):
    return (f'{self.name} has saved {self.money} money.')


import unittest

class WorkerTests(unittest.TestCase):

    def test_object_is_initializer(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(worker.name, 'Test')
        self.assertEqual(worker.salary, 100)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_work(self):
        worker = Worker('Test', 100, 10)
        worker.work()
        self.assertEqual(worker.money, 100)
        self.assertEqual(worker.energy, 9)

    def test_work_raises(self):
        worker = Worker('Test', 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest(self):
        worker = Worker('Test', 100, 0)
        worker.rest()
        self.assertEqual(worker.energy, 1)

    def test_get_info(self):
        worker = Worker('Test', 100, 0)
        self.assertEqual(worker.get_info(), 'Test has saved 0 money.')

if __name__ == '__main__':
    unittest.main()