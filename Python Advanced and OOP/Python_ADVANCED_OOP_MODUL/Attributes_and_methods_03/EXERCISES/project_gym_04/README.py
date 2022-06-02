"""
аз за всеки един файл без init и gym го бях направил така обаче judge ми даваше 95 точки:

class Customer:
    _id = 1     ТУК СЛАГАМ ДА ПОЧВА ОТ 1 (КАКТО Е ПО УСЛОВИЕ)

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer._id
        Customer._id += 1      ТУК УВЕЛИЧАВАМ ИД СЛЕД КАТО Е СЪЗДАДЕНА ВЕЧЕ ЕДНА ИНСТАНЦИЯ


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer._id    ТУК ПРОСТО ВРЪЩАМ ИД, КОЕТО АКО НЕ Е ИМАЛО ИНСТАНЦИЯ ЩЕ Е 1, АКО Е МИНАЛА ИНСТАНЦИЯ ЩЕ Е 2 И Т.Н.



    А във видеото е направено с долния(немаркирания) вариант и там дават 100 точки. Според мен логиката е еднаква, но при мен не работи.

"""

class Customer:
    _id = 0

    def __init__(self, name: str, address: str, email: str):
        Customer._id += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer._id


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer._id + 1

