from project.pokemon import Pokemon

"""
Pay attention to correct import path!!!!
"""

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if not pokemon in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        filtered_pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if filtered_pokemons:
            self.pokemon = [p for p in self.pokemon if not p.name == pokemon_name]
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\n" \
              f"Pokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            res += f'- {p.pokemon_details()}\n'
        return res

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())