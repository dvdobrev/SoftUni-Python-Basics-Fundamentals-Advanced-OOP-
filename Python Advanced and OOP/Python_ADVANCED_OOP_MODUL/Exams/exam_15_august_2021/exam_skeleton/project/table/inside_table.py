from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self._table_number = value

# i = InsideTable(3, 50)
# i.order_food(Bread("bql", 5))
# i.order_drink(Tea("black", 1, "nestea"))
# i.order_drink(Tea("black", 1, "nestea"))
# print(i.get_bill())
# i.clear()
# print(i.free_table_info())