from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_restaurant_05.product import Product

class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams
