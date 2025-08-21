from database import Database
from writeAJson import writeAJson

class Pokedex:
    def __init__(self, db):
        self.db = db

    def get_pokemon(self, name):
        result = self.db.get_pokemon(name)
        log = {"funcao": "get_pokemon", "parametros": {"name": name}, "resultado": result}
        writeAJson(log, f"log_get_pokemon_{name}.json")
        return result

    def get_all_pokemon(self):
        result = list(self.db.get_all_pokemon())
        log = {"funcao": "get_all_pokemon", "resultado": result}
        writeAJson(log, "log_get_all_pokemon.json")
        return result

    def get_pokemon_type(self, poke_type):
        result = self.db.get_pokemon_type(poke_type)
        log = {"funcao": "get_pokemon_type", "parametros": {"type": poke_type}, "resultado": result}
        writeAJson(log, f"log_get_pokemon_type_{poke_type}.json")
        return result

    def get_pokemon_level_above(self, level):
        result = self.db.get_pokemon_level_above(level)
        log = {"funcao": "get_pokemon_level_above", "parametros": {"level": level}, "resultado": result}
        writeAJson(log, f"log_get_pokemon_level_above_{level}.json")
        return result

    def get_pokemon_count(self):
        result = self.db.get_pokemon_count()
        log = {"funcao": "get_pokemon_count", "resultado": result}
        writeAJson(log, "log_get_pokemon_count.json")
        return result

db = Database()
pokedex = Pokedex(db)

print(pokedex.get_pokemon("Pikachu"))
print(pokedex.get_all_pokemon())
print(pokedex.get_pokemon_type("Fire"))
print(pokedex.get_pokemon_level_above(20))
print(pokedex.get_pokemon_count())