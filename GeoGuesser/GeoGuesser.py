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
            self.__locations.append(Location(float(longitude), float(latitutde), name, country))
    
    def ask_number_of_rounds(self):
        amount_of_rounds = input(f"How many rounds do u want to play?(1 -> {len(self.__locations)}) ")
        if  1 <= int(amount_of_rounds) <= len(self.__locations):
            self.__n_games = int(amount_of_rounds)
        else:
            print(f"This number is not an optoin({amount_of_rounds})")
            self.ask_number_of_rounds()
    

    def play_round(self, location):
        attempts = 2
        found = False
        while attempts > 0 and not found:
            print(f"Attempts left: {attempts}")
            if attempts > 1:
                print(location.question_hard())
            else:
                print(location.question_simple())
            guess_longitude = int(input("Longitude guess: "))
            guess_latitude = int(input("latitude guess: "))
            if location.verify_guess_is_close_enough(guess_longitude, guess_latitude):
                return True
            else:
                attempts -= 1
        return False
    

    def play_new_game(self, user):
        self.ask_number_of_rounds()
        game_running = True
        round = 0
        while game_running and round < self.__n_games:
            if self.play_round(self.__locations[round]):
               print(f"Yippie you found the location:\n {self.__locations[round].full_info()}")
               round += 1
               self.__score += 1
            else:
                game_running = False
        print(f"CONGRATS U FINISHED WITH A SCORE OF: {self.__score}")



    





Geoguesser = Game()
Geoguesser.load_locations_from_file("locations.txt")
Geoguesser.play_new_game("Quinten")
