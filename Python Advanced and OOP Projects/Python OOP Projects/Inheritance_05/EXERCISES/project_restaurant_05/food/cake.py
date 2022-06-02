from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_restaurant_05.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
