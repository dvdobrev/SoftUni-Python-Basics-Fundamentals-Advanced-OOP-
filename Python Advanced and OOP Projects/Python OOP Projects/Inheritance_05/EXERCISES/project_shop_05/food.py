from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_shop_05.product import Product


class Food(Product):
    def __init__(self, name, quantity=15):
        super().__init__(name, quantity)
        self.name = name
        self.quantity = 15
