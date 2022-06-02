from abc import ABC


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        pass

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return f"Woof!"


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return f"Meow meow!"


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender=None)
        self.gender = "Female"

    def make_sound(self):
        return f"Meow"


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender=None)
        self.gender = "Male"

    def make_sound(self):
        return f"Hiss"
