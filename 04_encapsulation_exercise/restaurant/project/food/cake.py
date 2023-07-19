from project.food.dessert import Desert

class Cake(Desert):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, 5, 250, 1000)