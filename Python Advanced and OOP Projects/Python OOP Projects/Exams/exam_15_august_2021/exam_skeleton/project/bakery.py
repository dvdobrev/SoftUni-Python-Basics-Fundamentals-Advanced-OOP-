from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []  # contain every type of food in the bakery's menu.
        self.drinks_menu = []  # contain every type of drink in the bakery's menu.
        self.tables_repository = []  # containing every table at the bakery.
        self.total_income = 0  # the total income from all the completed bills

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self._name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == "Bread":
            food = Bread(name, price)
            searched_food = [f for f in self.food_menu if f.name == name]
            if not searched_food:
                self.food_menu.append(food)
                return f"Added {food.name} ({food_type}) to the food menu"
            raise Exception(f"{food_type} {name} is already in the menu!")

        else:
            food = Cake(name, price)
            searched_food = [f for f in self.food_menu if f.name == name]
            if not searched_food:
                self.food_menu.append(food)
                return f"Added {food.name} ({food_type}) to the food menu"
            raise Exception(f"{food_type} {name} is already in the menu!")

    # def add_food(self, food_type: str, name: str, price: float):
    #     searched_food = [f for f in self.food_menu if f.name == name]
    #     if searched_food:
    #         raise Exception(f"{food_type} {name} is already in the menu!")
    #
    #     if food_type == "Bread":
    #         self.food_menu.append(Bread(name, price))
    #     elif food_type == "Cake":
    #         self.food_menu.append(Cake(name, price))
    #     return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
            searched_drink = [d for d in self.drinks_menu if d.name == name]
            if not searched_drink:
                self.drinks_menu.append(drink)
                return f"Added {drink.name} ({drink.brand}) to the drink menu"
            raise Exception(f"{drink_type} {name} is already in the menu!")

        else:
            drink = Water(name, portion, brand)
            searched_drink = [d for d in self.drinks_menu if d.name == name]
            if not searched_drink:
                self.drinks_menu.append(drink)
                return f"Added {drink.name} ({drink.brand}) to the drink menu"
            raise Exception(f"{drink_type} {name} is already in the menu!")

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
            searched_table = [t for t in self.tables_repository if t.table_number == table_number]
            if not searched_table:
                self.tables_repository.append(table)
                return f"Added table number {table_number} in the bakery"
            raise Exception(f"Table {table_number} is already in the bakery!")

        else:
            table = OutsideTable(table_number, capacity)
            searched_table = [t for t in self.tables_repository if t.table_number == table_number]
            if not searched_table:
                self.tables_repository.append(table)
                return f"Added table number {table_number} in the bakery"
            raise Exception(f"Table {table_number} is already in the bakery!")

    def reserve_table(self, number_of_people: int):
        try:
            free_table = [t for t in self.tables_repository if t.capacity >= number_of_people and not t.is_reserved][0]
            free_table.reserve(number_of_people)
            return f"Table {free_table.table_number} has been reserved for {number_of_people} people"

        except IndexError:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            food_not_in_menu = []
            for food_name in args:
                is_found = False
                for food in self.food_menu:
                    if food.name == food_name:
                        table.order_food(food)
                        is_found = True
                        break
                if not is_found:
                    food_not_in_menu.append(food_name)

            result = f"Table {table.table_number} ordered:\n"
            for food in table.food_orders:
                result += f"{repr(food)}\n"
            if food_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for food in food_not_in_menu:
                    result += f"{food}\n"

            return result

        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            drinks_not_in_menu = []
            for drink_name in args:
                is_found = False
                for drink in self.drinks_menu:
                    if drink.name == drink_name:
                        table.order_drink(drink)
                        is_found = True
                        break
                if not is_found:
                    drinks_not_in_menu.append(drink_name)

            result = f"Table {table.table_number} ordered:\n"
            for drink in table.drink_orders:
                result += f"{repr(drink)}\n"
            if drinks_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for drink in drinks_not_in_menu:
                    result += f"{drink}\n"

            return result

        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        searched_table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = searched_table.get_bill()
        self.total_income += bill
        searched_table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    # def get_free_tables_info(self):
    #     result = ""
    #     for table in self.tables_repository:
    #         result += table.free_table_info()
    #         result += "\n"
    #
    #     return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            result += f"{table.free_table_info()}\n"

        return result

    def get_total_income(self):

        return f"Total income: {self.total_income:.2f}lv"
