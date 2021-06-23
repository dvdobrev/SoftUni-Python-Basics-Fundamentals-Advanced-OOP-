from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_zoo_02.lizard import Lizard
from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_zoo_02.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)