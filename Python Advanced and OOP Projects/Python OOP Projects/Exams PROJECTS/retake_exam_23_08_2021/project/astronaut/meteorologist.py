from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    default_oxygen = 90
    breath_reduce_oxygen = 15

    def __init__(self, name):
        super().__init__(name, self.default_oxygen)


# a = Meteorologist("dobri", 10)
# print(a.default_oxygen)
# a.breathe()
# print(a.oxygen)
#
