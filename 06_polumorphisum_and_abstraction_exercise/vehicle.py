from abc import ABC, abstractmethod


class Vehicle():
    def __init__(self, fuel_capacity, fuel_consumption):
        self.fuel_quantity = fuel_capacity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONDITION = 0.9

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Car.CONDITION)
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

        def refuel(self, fuel):
            self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITION = 1.6

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Truck.CONDITION)
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
