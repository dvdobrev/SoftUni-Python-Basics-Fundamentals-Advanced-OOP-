from Python_ADVANCED_OOP_MODUL.Encapsulation_04.EXERCISES.project_wild_cat_zoo_01.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age)
        # self.name = name
        # self.gender = gender
        # self.age = age


    def get_needs(self):
        return 50


    # def __repr__(self):
    #     return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

