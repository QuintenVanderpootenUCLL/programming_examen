# Opgave: GeoGuesser Spel

GeoGuessr is een spel waarin spelers locaties moeten raden op basis van Street View-beelden. In deze oefening gaan wij een eenvoudigere variant hiervan bouwen.

De gebruiker zal een welbepaalde locatie te zien krijgen en proberen gokken waar deze ligt, door de lengte- en breedtegraad in te voeren. De speler krijgt steeds 2 pogingen: eerst enkel met de specifieke locatie, zonder het land, en de tweede keer met het land meegegeven. Een voorbeelduitvoer van het spel kan je hieronder vinden.

``` lang-none
Starting a new game for Ruben...

How many locations would you like to try to guess? (max = 20, default = 5)

5 locations left, your current score is 0


Attempts left: 2

Jakarta:
Longitude guess: 2
Latitude guess: 2

Try again...


Attempts left: 1

Jakarta, Indonesia:
Longitude guess: 6
Latitude guess: 2

Too bad! The answer was Indonesia, Jakarta: (-6.21,106.85)


---------------------------------------


4 locations left, your current score is 0


Attempts left: 2

Seoul:
Longitude guess: 37
Latitude guess: 126

Congratulations! The answer was South Korea, Seoul: (37.57,126.98)


---------------------------------------


3 locations left, your current score is 2


Attempts left: 2

Rome:
Longitude guess: 5
Latitude guess: 9

Try again...


Attempts left: 1

Rome, Italy:
Longitude guess: 5
Latitude guess: 9

Too bad! The answer was Italy, Rome: (41.90,12.50)


---------------------------------------


2 locations left, your current score is 2


Attempts left: 2

Buenos Aires:
Longitude guess: 3
Latitude guess: 3

Try again...


Attempts left: 1

Buenos Aires, Argentina:
Longitude guess: -34
Latitude guess: -58

Congratulations! The answer was Argentina, Buenos Aires: (-34.60,-58.38)


---------------------------------------


1 location left, your current score is 3


Attempts left: 2

Berlin:
Longitude guess: 5
Latitude guess: 3

Try again...


Attempts left: 1

Berlin, Germany:
Longitude guess: 4
Latitude guess: 3

Too bad! The answer was Germany, Berlin: (52.52,13.40)


---------------------------------------


Game over! Final score for Ruben: 3
```

Om het spel te kunnen spelen hebben we twee klassen nodig. De klasse `Location` en de klasse `Game`.

## Location

Deze klasse stelt een geografische locatie voor. Elke locatie bevat volgende informatie. Om het spel spannend te houden zijn de `longitude` en `latitude` waarden niet zichtbaar van buitenaf.

- `longitude`: De lengtegraad van de locatie.
- `latitude`: De breedtegraad van de locatie.
- `name`: De naam van de locatie.  
- `country`: Het land waarin de locatie zich bevindt.  

``` lang-none
>>> ny = Location(40.7128, -74.0060, "New York", "USA")
>>> ny.name
New York
>>> ny.country
USA
>>> ny.latitude
AttributeError: 'Location' object has no attribute 'latitude'
>>> ny.longitude
AttributeError: 'Location' object has no attribute 'longitude'
```

Methoden:

1. `verify_guess_is_close_enough(longitude, latitude)`  
   - Controleert de gegeven lengte- en breedtegraad.
   - We hanteren voor deze oefening dat de lengte- en breedtegraad binnen een bereik van één graad van de werkelijke coördinaten moet liggen.
   - Deze functie zal een `bool` returnen.

2. `question_hard()`  
   - Retourneert een string in het format: `"<name>:"`. Dit geeft een aanwijzing aan de gebruiker.

3. `question_simple()`  
   - Retourneert een string in het format: `"<name>, <country>:"`. Dit geeft een aanwijzing aan de gebruiker.

4. `full_info()`  
   - Retourneert de volledige informatie over de locatie, inclusief coördinaten, in onderstaand format met steeds twee cijfers na de komma voor de coördinaten:  
     `"<country>, <name>: (<longitude>, <latitude>)"`.

``` lang-none
>>> ny.question_hard()
New York:
>>> ny.question_simple()
New York, USA:
>>> ny.full_info()
USA, New York: (40.71,-74.01)
>>> print(ny.verify_guess_is_close_enough(25,-90))
False
>>> print(ny.verify_guess_is_close_enough(40,-75))
True
```

## Game

Deze klasse simuleert het spel. Ieder spel bevat volgende informatie:

- Een collectie `locations` van `Location`-objecten die moeten worden geraden. Bij het aanmaken van een Game object zijn er nog geen locaties aanwezig.
- Een `score` dat het aantal behaalde punten bijhoudt. Deze start op 0 bij een nieuw spel.
- Het aantal rondes `n_games` die gespeeld worden. De default waarde hiervan is 5 rondes.

``` lang-none
>>> geoguesser = Game()
>>> geoguesser.locations
AttributeError: 'Game' object has no attribute 'locations'
>>> geoguesser.n_games
AttributeError: 'Game' object has no attribute 'n_games'
>>> geoguesser.score
0
>>> geoguesser.score = 100
AttributeError: property 'score' of 'Game' object has no setter
```

Methoden:  

1. `load_locations_from_file(filename)`  
   - Leest een bestand met locatiegegevens. Elke regel bevat de naam van een locatie, het land, de lengtegraad, en de breedtegraad in het format:  
     `"<name>, <country>, <longitude>, <latitude>"`.  
   - Maakt een `Location`-object voor elke regel en voegt dit toe aan de collectie van locaties.

2. `ask_number_of_rounds()`
   - Vraagt de gebruiker hoeveel rondes deze wilt spelen. Het default aantal is 5. Het maximale aantal is het aantal locaties in `locations`.

3. `play_round(location)`
   - Gebruikers krijgen 2 pogingen om voor de parameter locatie een juiste gok in te voeren. Bij de eerste poging wordt enkel de plaatsnaam gegeven, voor de tweede poging wordt daarbij ook het land getoond.
   - Bij juiste invoer wordt de de score verhoogd. De speler krijgt 2 punten als die het in één poging kon raden, anders maar 1 punt.
   - Na 2 foutieve pogingen wordt de locatie overgeslagen, en de juiste coördinaten worden getoond.

4. `play_new_game(user)`  
   - Start een nieuw spel voor een opgegeven gebruiker.
   - Vraag de gebruiker hoeveel rondes deze wilt spelen. Maak gebruik van eerder gemaakte methodes.
   - Speel het aantal rondes dat door de gebruiker gespecifieerd werd. Maak gebruik van de eerder gemaakte methodes.
   - Het spel eindigt wanneer er geen locaties meer over zijn of de limiet van aantal spellen is bereikt.
   - Toon de eindscore.

## Test het programma

Gebruik de gegevens in het bestand `locations.txt` om het programma te testen door onderstaande code toe te voegen aan jouw oplossing:  

```Python
geoguesser = Game()
geoguesser.load_locations_from_file("locations.txt")
geoguesser.play_new_game("Ruben") # Hier kan je uiteraard jouw naam invullen
```

Start een nieuw spel voor een gebruiker en voer enkele schattingen in. Veel spelplezier gewenst!
