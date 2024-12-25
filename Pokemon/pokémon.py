class Pokemon():
    def __init__(self, number, name, type):
        self.number = number
        self.name = name
        self.type = type
        self.name_found = False
        self.type_found = False


class Pokedex():
    def __init__(self):
        self.pokemons = {}
    
    def add_pokemon(self, number, name, type):
        self.pokemons[name.lower()] = Pokemon(number, name, type)
    
    def get_pokemon(self, name):
        return self.pokemons[name.lower()]
    
    def add_progress(self, name, type):
        pokemon = self.pokemons.get(name.lower(), "error")
        if pokemon == "error":
            raise ValueError(f"This pokémon doesn't exist {name}")
        pokemon.name_found = True
        if type != None:
            pokemon.type_found = True
    
    def check_pokemon(self, name, type):
        pokemon = self.pokemons.get(name.lower(), "error")
        if pokemon == "error":
            print(f"{name} is not the name of a pokemon")
        
        if pokemon.name_found:
            message1 = f"You have allready found {pokemon.name}"
        elif pokemon.name == name:
            pokemon.name_found = True
            message1 = f"Congratulations. You found Ratata"
        
        if type == None:
            message2 = ""
        if pokemon.type_found:
            message2 = f"You have allready found the typing of {pokemon.name}"
        if type == pokemon.type:
            pokemon.type_found = True
            message2 = f"Congratsulaton you found the type for pokemon {pokemon.name}"
        else:
            message2 = f"{type} is not the correct type for the pokemon {pokemon.name}"
        
        print(f"{message1} -- {message2}")

    
    def print_overview(self):
        print("####################################")
        print("####################################")
        for pokemon in self.pokemons.values():
            if pokemon.name_found:
                name = pokemon.name
            else:
                name = "???"
            
            if pokemon.type_found:
                type = pokemon.type
            else:
                type = "???"
            print(f"{pokemon.number} / {name} / {type}")
        
        print("####################################")
        print("####################################")


    def read_pokemon_data(self, file):
       pokemonlist = []
       with open(file, "r", encoding= "utf-8") as pokemon_data:
            for line in pokemon_data:
                pokemon = line.strip("\n").split(",")
                pokemonlist.append(tuple(pokemon))
            print(pokemonlist)

           
        







        




pokedex = Pokedex()
# pokedex.add_pokemon("#0001", "Bulbasaur", "Grass-Poison")
# pokedex.add_progress("Bulbasaur", "Grass-Poison")
# pokedex.add_pokemon("#0003", "Ratata", "Normal")
# bulbasaur = pokedex.get_pokemon("Bulbasaur")
# print(bulbasaur.name_found)

# pokedex.add_pokemon("#0002", "Pidgey", "Normal-Flying")
# pokedex.add_progress("Pidgey", None)
# pidgey = pokedex.get_pokemon("Pidgey")
# print(pidgey.name_found, pidgey.type_found)
# pokedex.check_pokemon("Pidgey", "Normal-Flying")
# print(pidgey.name_found, pidgey.type_found)
# pokedex.check_pokemon("Ratata", None)
# pokedex.check_pokemon("Ratata", "Grass")
# #pokedex.check_pokemon("Ratata", "Normal")
# pokedex.print_overview()
pokedex.read_pokemon_data("pokemons.txt")


