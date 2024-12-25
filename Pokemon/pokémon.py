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
            return None
        
        if pokemon.name_found:
            message1 = f"You have allready found {pokemon.name}"

        elif pokemon.name.lower() == name.lower():
            pokemon.name_found = True
            message1 = f"Congratulations. You found {pokemon.name}"
        
        if type == None:
            message2 = f"You didn't guess a type this time"
        elif pokemon.type_found:
            message2 = f"You have allready found the typing of {pokemon.name}"
        elif type.lower() == pokemon.type.lower():
            pokemon.type_found = True
            message2 = f"Congratulations you found the type for the pokemon {pokemon.name}"
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
        for pokémon in pokemonlist:
            number , name , type  = pokémon
            self.add_pokemon(number, name, type)
  
    def write_progress(self):
        pokemons = self.pokemons.values()
        first = True
        with open("progress.txt", "w", encoding="utf-8") as progress_file:
            for pokemon in pokemons:
                string  = ""
                if pokemon.name_found:
                    if not first:
                        string += "\n"
                    string += pokemon.name
                    if pokemon.type_found:
                        string += f",{pokemon.type}"
                    if first:
                        first = False
                    progress_file.write(string)


    def read_progress_data(self):
        with open("progress.txt", "r", encoding= "utf-8") as progress_file:
            lines = progress_file.readlines()
        for pokemon in lines:
            data = pokemon.strip("\n").split(",")
            if len(data) == 1:
                self.add_progress(data[0], None)
            else:
                self.add_progress(data[0], data[1])


        



def start_game():
    pokedex = Pokedex()
    playing = True
    pokedex.read_pokemon_data("pokemons.txt")
    pokedex.read_progress_data()
    while playing:
        choice = input("What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? ").strip().upper()
        if choice == "G":
            guess_name = input("Guess a pokemon's name ")
            guess_type = input("Guess the type of the pokemon u just named or type nothing if u don't know ")
            if guess_type == "":
                guess_type = None
            pokedex.check_pokemon(guess_name, guess_type)
        
        elif choice == "S":
            pokedex.print_overview()
        

        elif choice == "Q":
            pokedex.write_progress()
            playing = False
        
        else:
            print(f"This is not a valid choice {choice}")
    

start_game()
