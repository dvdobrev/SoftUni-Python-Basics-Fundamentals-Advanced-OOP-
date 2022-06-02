from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    default_oxygen = 70
    breath_reduce_oxygen = 5

    def __init__(self, name):
        super().__init__(name, self.default_oxygen)


# a = Biologist("dobri", 10)
# print(a.default_oxygen)
# a.breathe()
# print(a.oxygen)
