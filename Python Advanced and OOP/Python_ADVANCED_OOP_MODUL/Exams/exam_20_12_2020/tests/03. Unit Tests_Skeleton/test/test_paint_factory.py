from unittest import TestCase, main

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.f1 = PaintFactory("factory_1", 10)
        self.f1.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        self.f1.ingredients = {"red": 1, "blue": 2}
        self.product_type_green = "green"
        self.green_product_quantity = 2
        self.product_type_white = "white"
        self.test_product_quantity = 100

    def test_init(self):
        self.assertEqual("factory_1", self.f1.name)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.f1.valid_ingredients)

    def test_add_ingredient_product_type_is_in__valid_ingredients(self):
        self.f1.add_ingredient(self.product_type_green, self.green_product_quantity)
        result = [p for p in self.f1.valid_ingredients if p == "red"][0]
        self.assertEqual("red", result)

    def test_add_ingredient_product_type_is_not_in__valid_ingredients(self):
        with self.assertRaises(TypeError) as ex:
            self.f1.add_ingredient("pink", 10)
        self.assertEqual(f"Ingredient of type pink not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_product_type_is_in__valid_ingredients_and__can_add_product_quantity_and_product_not_in_ingredients(
            self):
        product_type = [p for p in self.f1.valid_ingredients if p == self.product_type_green][0]
        self.assertEqual("green", product_type)

        result = self.f1.can_add(1)
        self.assertEqual(True, result)

        product_not_in_ingredients = [p for p in self.f1.ingredients if p == "green"]
        self.assertEqual(0, len(product_not_in_ingredients))

        self.f1.add_ingredient(self.product_type_green, self.green_product_quantity)

    def test_add_ingredient_product_type_is_in__valid_ingredients_and__can_NOT_add_product_quantity(
            self):
        self.green_product_quantity = 8
        product_type = [p for p in self.f1.valid_ingredients if p == self.product_type_green][0]
        self.assertEqual("green", product_type)

        with self.assertRaises(ValueError) as ex:
            self.f1.add_ingredient(self.product_type_green, self.green_product_quantity)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_remove_ingredient_when_product_type_is_in_ingredients_and_is_greater_than_zero(self):
        self.f1.add_ingredient(self.product_type_green, self.green_product_quantity)
        self.f1.add_ingredient(self.product_type_green, 3)

        result_product_type = [p for p in self.f1.ingredients if p == self.product_type_green]
        self.assertEqual(1, len(result_product_type))

        self.f1.remove_ingredient(self.product_type_green, 1)

    def test_remove_ingredient_when_product_type_is_in_ingredients_and_is_less_than_zero(self):
        self.f1.add_ingredient(self.product_type_green, self.green_product_quantity)

        result_product_type = [p for p in self.f1.ingredients if p == self.product_type_green]
        self.assertEqual(1, len(result_product_type))

        with self.assertRaises(ValueError) as ex:
            self.f1.remove_ingredient(self.product_type_green, 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_when_product_NOT_in_ingredients(self):
        with self.assertRaises(KeyError) as ex:
            self.f1.remove_ingredient(self.product_type_white, 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))


if __name__ == '__main__':
    main()
