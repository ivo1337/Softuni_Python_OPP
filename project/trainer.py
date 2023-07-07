from typing import List
from project.pokemon import Pokemon



class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        except IndexError:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])
        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())


from project.pokemon import Pokemon
from project.trainer import Trainer

import unittest


class PokemonTest(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer("Ash")
        self.pokemon = Pokemon("Pikachu", 90)
        self.second_pokemon = Pokemon("Charizard", 110)

    def test_pokemon_init(self):
        message = self.pokemon.pokemon_details()
        expected = "Pikachu with health 90"
        self.assertEqual(message, expected)

    def test_adding_pokemon(self):
        message = self.trainer.add_pokemon(self.pokemon)
        expected = "Caught Pikachu with health 90"
        self.assertEqual(message, expected)

    def test_adding_second_pokemon(self):
        message = self.trainer.add_pokemon(self.second_pokemon)
        expected = "Caught Charizard with health 110"
        self.assertEqual(message, expected)

    def test_adding_already_added_pokemon(self):
        self.trainer.add_pokemon(self.second_pokemon)
        message = self.trainer.add_pokemon(self.second_pokemon)
        expected = "This pokemon is already caught"
        self.assertEqual(message, expected)

    def test_releasing_pokemon(self):
        self.trainer.add_pokemon(self.pokemon)
        message = self.trainer.release_pokemon("Pikachu")
        expected = "You have released Pikachu"
        self.assertEqual(message, expected)

    def test_releasing_pokemon_that_is_not_caught(self):
        message = self.trainer.release_pokemon("Pikachu")
        expected = "Pokemon is not caught"
        self.assertEqual(message, expected)

    def test_trainer_data(self):
        self.trainer.add_pokemon(self.pokemon)
        self.trainer.add_pokemon(self.second_pokemon)
        self.trainer.release_pokemon("Pikachu")
        message = self.trainer.trainer_data()
        message = message.strip('\n')
        expected = "Pokemon Trainer Ash\nPokemon count 1\n- Charizard with health 110"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()