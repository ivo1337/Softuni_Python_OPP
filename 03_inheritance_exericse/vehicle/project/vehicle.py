class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel: float = fuel
        self.horse_power: int = horse_power

    def drive(self, kilometers: int):
        fuel_needed: float = kilometers * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed