from math import sqrt
def bereken_afstand(coordinaat1, coordinaat2):
        return sqrt((coordinaat2[0] - coordinaat1[0])**2 + (coordinaat2[1] - coordinaat1[1])**2)

def read_animal_data(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    animal = {}
    for line in lines:
        splitted = line.strip("\n").split(",")
        animal[splitted[0]] = splitted[1]
    return animal


def read_location_data(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    locations = {}
    for line in lines:
        splitted = line.strip("\n").split(",")
        animal = locations.get(splitted[1], None)
        if animal == None:
            locations[splitted[1]] = [(splitted[0], int(splitted[2]), int(splitted[3]))]
        else:
            animal.append((splitted[0], int(splitted[2]), int(splitted[3])))
    
    return locations

def calculate_travelled_distance(locatie_data):
    afstand = 0
    vorige_locatie = (locatie_data[0][1], locatie_data[0][2])
    for i in range(1, len(locatie_data)):
        nieuwe_locatie = (locatie_data[i][1], locatie_data[i][2])
        afstand += bereken_afstand(vorige_locatie, nieuwe_locatie)
        vorige_locatie = nieuwe_locatie
    return afstand

def most_active_animal(location_data):
    afstand_per_dier = {}
    afstanden = set()
    for dier, locaties in location_data.items():
        afstand = calculate_travelled_distance(locaties)
        afstand_per_dier[afstand] = dier
        afstanden.add(afstand)
    maximale_afstand = max(afstanden)
    return (afstand_per_dier[maximale_afstand], maximale_afstand)


def most_lazy_animal(location_data):
    afstand_per_dier = {}
    afstanden = set()
    for dier, locaties in location_data.items():
        afstand = calculate_travelled_distance(locaties)
        afstand_per_dier[afstand] = dier
        afstanden.add(afstand)
    maximale_afstand = min(afstanden)
    return (afstand_per_dier[maximale_afstand], maximale_afstand)


def flag_predator_prey_contact(location_data, animal_data):
    def is_predator_or_prey(animal):
        predators = {"Lion", "Tiger", "Bear", "Snake", "Crocodile", "Panther"}
        if animal in predators:
            return "Predator"
        else:
            return "Prey"
    with open("contacts.txt", "w", encoding="utf-8"):
            pass
    for animal1 in location_data.items():
        naam1 , locaties1 = animal1
        if is_predator_or_prey(animal_data[naam1]) == "Predator":
            for animal2 in location_data.items():
                naam2, locaties2 = animal2
                if is_predator_or_prey(animal_data[naam2]) == "Prey" and naam2 != naam1:
                    for i in range(0, len(locaties1)):
                        tijdstip, x1, y1 = locaties1[i]
                        tijdstip, x2, y2 = locaties2[i]
                        afstand = bereken_afstand((x2,y2),(x1,y1))
                        if afstand <= 2:
                            with open("contacts.txt", "a", encoding="utf-8") as file:
                                file.write(f"Time {tijdstip}, {naam1} ({animal_data[naam1]}), {naam2} ({animal_data[naam2]}), Distance {afstand}\n")

                         


        

   




animal_data = read_animal_data("animals.txt")
location_data = read_location_data("locations.txt")

most_active, active_distance = most_active_animal(location_data)
print(f"Most active animal: {most_active} with distance {active_distance:.2f}")
"Most active animal: Gallop with distance 1548.18"

most_lazy, lazy_distance = most_lazy_animal(location_data)
print(f"Most lazy animal: {most_lazy}with distance {lazy_distance:.2f}")
"Most lazy animal: Tower with distance 971.62"

flag_predator_prey_contact(location_data, animal_data)
print("Contacts between predators and prey are saved in 'contacts.txt'.")