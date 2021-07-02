from typing import List


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        searched_product = [p for p in self.products if p.name == product_name][0]
        return searched_product

    def remove(self, product_name):
        self.products = [p for p in self.products if not p.name == product_name]
        return self.products

    def __repr__(self):
        result = '\n'.join([(f"{el.name}: {el.quantity}") for el in self.products])
        return result
