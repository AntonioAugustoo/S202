class Database:
    def __init__(self):
        self.data = {
            "Pikachu": {"type": "Electric", "level": 25},
            "Charmander": {"type": "Fire", "level": 20},
            "Bulbasaur": {"type": "Grass", "level": 18},
            "Squirtle": {"type": "Water", "level": 22},
            "Eevee": {"type": "Normal", "level": 15},
        }

    def get_pokemon(self, name):
        return self.data.get(name)

    def get_all_pokemon(self):
        return self.data.keys()

    def get_pokemon_type(self, poke_type):
        return [name for name, info in self.data.items() if info["type"] == poke_type]

    def get_pokemon_level_above(self, level):
        return [name for name, info in self.data.items() if info["level"] > level]

    def get_pokemon_count(self):
        return len(self.data)