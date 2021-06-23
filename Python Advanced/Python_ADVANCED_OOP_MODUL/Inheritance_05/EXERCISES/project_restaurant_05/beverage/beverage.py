from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_restaurant_05.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters
