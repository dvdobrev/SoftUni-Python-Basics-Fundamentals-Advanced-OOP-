from project.drink.drink import Drink


class Water(Drink):
    default_price = 1.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.default_price, brand)


# w = Water("water", 200, "devin")
# print(w)