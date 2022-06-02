from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    default_oxygen = 50
    breath_reduce_oxygen = 10

    def __init__(self, name):
        super().__init__(name, self.default_oxygen)


#
# a = Geodesist("dobri")
# print(a.default_oxygen)
# a.breathe()
# print(a.oxygen)
