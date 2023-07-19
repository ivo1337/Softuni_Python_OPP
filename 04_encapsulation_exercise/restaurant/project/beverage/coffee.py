from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    def __init__(self, name, caffeine):
        super().__init__(name, 3.50, 50)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine