from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_players_and_monsters_03.elf import Elf
from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_players_and_monsters_03.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)