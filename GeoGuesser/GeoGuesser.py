class Location():
    def __init__(self, longitude, latitude, name, country):
        self.__longtitude = longitude
        self.__latitude = latitude
        self.name = name
        self.country = country

    def verify_guess_is_close_enough(self, longitude, latitude):
        return (abs(longitude - self.__longtitude)) <= 1 and (abs(latitude - self.__latitude)) <= 1
        
    def question_hard(self):
        return f"{self.name}:"
    
    def question_simple(self):
        return f"{self.name}, {self.country}:"
    
    def full_info(self):
        return f"{self.country}, {self.name}: ({self.__longtitude}, {self.__latitude})"


class Game():
    def __init__(self):
        self.__locations = []
        self.__n_games = 5
        self.__score = 0

    @property
    def score(self):
        return self.__score
    

    def load_locations_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip("\n").split(", ")
            name, country, longitude, latitutde = line
            self.__locations.append(Location(longitude, latitutde, name, country))
    
    def ask_number_of_rounds(self):
        amount_of_rounds = input(f"How many rounds do u want to play?(1 -> {len(self.__locations)}) ")
        if  1 <= int(amount_of_rounds) <= len(self.__locations):
            self.__n_games = amount_of_rounds
        else:
            print(f"This number is not an optoin({amount_of_rounds})")
            self.ask_number_of_rounds()
    


    





Geoguesser = Game()
Geoguesser.load_locations_from_file("locations.txt")
Geoguesser.ask_number_of_rounds()
