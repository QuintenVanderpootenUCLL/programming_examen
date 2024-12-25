# Pokedex
In deze oefening gaan we een python-script schrijven om een Pokemon spelletje te spelen. Alle 151 Pokemons worden opgeladen in onze Pokedex en daarna is het aan jou om te bewijzen dat je ze alle 151 kan raden. En de echte Pokemon-experts kennen ook het type van alle Pokemons. Slaag jij erin om ze allemaal te raden? Bewijs jij dat je de expert bent...

```
What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? G
Please enter the name of the Pokemon: Pikachu
Please enter the type for this Pokemon (leave blank if you don't want to guess the type):
>>> Congratulations. You have found pikachu
What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? G
Please enter the name of the Pokemon: Pikachu
Please enter the type for this Pokemon (leave blank if you don't want to guess the type): Electric
>>> You have already found the pokemon pikachu - Congratulations, You have found the type for pokemon pikachu
What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? G
Please enter the name of the Pokemon: Raichu
Please enter the type for this Pokemon (leave blank if you don't want to guess the type): Electric
>>> Congratulations. You have found raichu - Congratulations, You have found the type for pokemon raichu
```

## Class Pokemon
Een Pokemon heeft in onze oefening drie eigenschappen: Een nummer (vb. #0001, #0002, ...), een naam (vb. Squirtle, Pikachu, ...) en een type (vb. Grass, Grass-Poison, Electric, ...).

Sommige Pokemon hebben officieel 2 types (vb. Bulbasaur heeft de types Grass en Poison). Omdat we echte Pokemon-nerds zijn, willen we dit ook ondersteunen. Maar omdat we het ook niet te moeilijk willen maken, stellen we de 2 types voor door ze als string te combineren met een streep (-) ertussen. Je kan dus stellen dat Bulbasaur eigenlijk 1 type heeft, namelijk Grass-Poison.

Om te starten gaan we een klasse `Pokemon` maken. Wanneer we een `Pokemon` aanmaken, willen we een nummer, naam en type kunnen meegeven:

```python
>>> bulbasaur = Pokemon("#0001", "Bulbasaur", "Grass-Poison")
>>> bulbasaur.name
"Bulbasaur""
>>> bulbasaur.number
"#0001"
>>> bulbasaur.type
"Grass-Poison"
```

Verder willen we ook van elke Pokemon de volgende info kunnen bijhouden:
- Heeft de speler de naam van deze pokemon al geraden?
- Heeft de speler het type van deze pokemon al geraden?

Initieel worden deze attributen op False gezet.

```python
>>> bulbasaur.name_found
False
>>> bulbasaur.type_found
False
```

## Class Pokedex
De Pokedex is de verzameling waar we alle info over onze Pokemon gaan bijhouden en waar we ook een aantal methodes zullen implementeren om te interageren met de Pokedex.

Om dit te doen maken we een klasse `Pokedex` aan. Wanneer we een instantie maken van deze klasse, geven we geen argumenten mee. We zullen hier later zaken aan toevoegen.

```python
>>> pokedex = Pokedex()
```

### Pokemon toevoegen en opvragen
Om onze Pokedex gebruiksklaar te maken, moeten we natuurlijk eerst onze Pokemon gaan toevoegen.
Definieer een methode `add_pokemon` die een nummer, naam en type als argument neemt en deze pokemon toevoegt aan onze Pokedex.

```python
>>> pokedex.add_pokemon("#0001", "Bulbasaur", "Grass-Poison")
```

Zoals je kan zien, zal er een nieuw `Pokemon` object aangemaakt worden wanneer een Pokemon toegevoegd wordt aan de Pokedex.

Om het resultaat hiervan te zien, moeten we ook een methode `get_pokemon` voorzien die een pokemon naam als argument neemt, en het geassocieerde Pokemon object teruggeeft:

```python
>>> bulbasaur = pokedex.get_pokemon("Bulbasaur")
>>> bulbasaur.name
"Bulbasaur"
>>> bulbasaur.type
"Grass-Poison"
```

### Informatie over gevonden toevoegen
We moeten voor een bepaalde Pokemon uit onze Pokedex kunnen aangeven dat we zijn naam en/of type reeds geraden hebben. Schrijf hiervoor een methode `add_progress` die een naam en type ontvangt. Als onze Pokedex een Pokemon met de gegeven naam bevat, dan zetten we de `name_found` eigenschap op True. Als het type argument niet None is, dan zetten we ook de `type_found` eigenschap op True. Als onze Pokedex geen Pokemon met de gegeven naam bevat, dan gooien we een `ValueError`.

```python
>>> pokedex.add_progress("Bulbasaur", "Grass-Poison")
>>> bulbasaur = pokedex.get_pokemon("Bulbasaur")
>>> bulbasaur.name_found
True
>>> bulbasaur.type_found
True
>>> pokedex.add_progress("Pidgey", None)
>>> pidgey = pokedex.get_pokemon("Pidgey")
>>> pidgey.name_found
True
>>> pidgey.type_found
False
```

### Checken van een Pokemon  gok
We kunnen een gokje wagen om de naam en het type van een Pokemon te vinden. Hiervoor schrijven we een methode `check_pokemon` die als argumenten een naam en eventueel een type neemt (indien er geen gok gebeurd is voor het type, wordt None meegegeven). De methode zal een string teruggeven die de feedback van onze gok zal bevatten.

Er zijn een aantal mogelijkheden, die we elk apart moeten afchecken:

* De meegegeven naam behoort niet tot een Pokemon uit onze Pokedex

```python
>>> pokedex.check_pokemon("Some Name", None)
"Some Name is not the name of a Pokemon"
```

* De meegegeven naam behoort tot een pokemon die we reeds gevonden hadden
  * We hebben geen type meegegeven
  * We hebben reeds de types gevonden voor deze pokemon
  * Het meegegeven type komen niet overeen met het type van de pokemon
  * Het meegegeven type komen overeen met het type van de pokemon

```python
>>> bulbasaur = pokedex.get_pokemon("Bulbasaur")
>>> (bulbasaur.name_found, bulbasaur.type_found)
(True, True)

>>> pidgey = pokedex.get_pokemon("Pidgey")
>>> (pidgey.name_found, pidgey.type_found)
(True, False)

>>> pokedex.check_pokemon("Bulbasaur", None)
"You have already found Balbusaur"

>>> pokedex.check_pokemon("Bulbasaur", "Grass-Poison")
"You already found the type for pokemon Bulbasaur, so your guesses were ignored"

>>> pokedex.check_pokemon("Pidgey", "Grass")
"You have already found Pigdey - Grass is not the correct type for pokemon Pidgey"

>>> pokedex.check_pokemon("Pidgey", "Normal-Flying")
"You have already found Pigdey - Congratulations, You have found the type for pokemon Pidgey"

>>> pidgey = pokedex.get_pokemon("Pidgey")
>>> (pidgey.name_found, pidgey.type_found)
(True, True)
```

* De meegegeven naam behoort tot een pokemon die we nog niet gevonden hadden
  * We hebben geen type meegegeven
  * Het meegegeven type komen niet overeen met het type van de pokemon
  * Het meegegeven type komen overeen met het type van de pokemon

```python
>>> rattata = pokedex.get_pokemon("Rattata")
>>> (rattata.name_found, rattata.type_found)
(False, False)

>>> pokedex.check_pokemon("Rattata", None)
"Congratulations. You have found Rattata"

>>> rattata = pokedex.get_pokemon("Rattata")
>>> (rattata.name_found, rattata.type_found)
(True, False)

>>> raticate = pokedex.get_pokemon("Raticate")
>>> (raticate.name_found, raticate.type_found)
(False, False)

>>> pokedex.check_pokemon("Raticate", "Grass")
"Congratulations. You have found Raticate - Grass is not the correct type for pokemon Raticate"

>>> raticate = pokedex.get_pokemon("Raticate")
>>> (raticate.name_found, raticate.type_found)
(True, False)

>>> spearow = pokedex.get_pokemon("Spearow")
>>> (spearow.name_found, spearow.type_found)
(False, False)

>>> pokedex.check_pokemon("Spearow", "Normal-Flying")
"Congratulations. You have found Spearow - Congratulations, You have found the type for pokemon Spearow"

>>> spearow = pokedex.get_pokemon("Spearow")
>>> (spearow.name_found, spearow.type_found)
(True, True)
```

### Tonen van alle gevonden pokemon
Nu dat we in staat zijn om Pokemon en hun type te raden, willen we een mooi overzicht krijgen van alle Pokemon die we al geraden hebben.

We zullen een methode `print_overview` implementeren die alle Pokemon toont en aangeeft welke informatie we al hebben geraden.

```python
>>> print(pokedex.display_pokedex())
####################
####################
#0001 | Bulbasaur | Grass-Poison
#0002 | ??? | ???
...
#0016 | Pidgey | Normal-Flying
...
#0019 | Rattata | ???
#0020 | Raticate | ???
#0021 | Spearow | Normal-Flying
...
#0150 | ??? | ???
#0151 | ??? | ???
####################
####################
```

## Pokemon Data
Om pokemon en hun type te kunnen raden, moet ons programma natuurlijk eerst weten welke pokemon er allemaal zijn. Laten we nu even kijken hoe we de Pokemon data van alle 151 originele pokemon kunnen lezen uit een file.

### File formaat
In deze folder staat een file genaamd `pokemons.txt`, dewelke alle informatie bevat van de 151 originele Pokemon. Elke lijn in de file is als volgt geformatteerd:
```
<nummer>,<naam>,<type>
```
Bekijk zeker de file om het formaat beter te verstaan.

### Het lezen van de Pokemon data
Laat ons om te beginnen een functie `read_pokemon_data` schrijven die zo'n bestand kan lezen en die een lijst teruggeeft met alle gevonden Pokemon. De functie geeft een lijst van tuples terug, waar elke tuple als volgt is opgesteld (nummer, naam, type):

```python
>>> read_pokemon_data('pokemons.txt')
[('#0001', 'Bulbasaur', "Grass-Poison"),
 ('#0002', 'Ivysaur', "Grass-Poison"),
 ...
 ('#0151', 'Mew', "Psychic")]
```

## Opslaan van vooruitgang
Aangezien we waarschijnlijk niet alle pokemon in één sessie gaan raden, zouden we de vooruitgang die we in een sessie maken graag bewaren, zodat we in de volgende sessie kunnen beginnen waar we gestopt waren. Daarom zullen we in een bestand 'progress.txt' bijhouden welke Pokemon we al geraden hebben. Zo kunnen we de volgende keer verder gaan met de situatie zoals ze was bij het eindigen van het spel.

### File formaat
In deze folder staat een file genaamd `progress.txt`, dewelke alle informatie bevat van alle geraden Pokemon en hun type. Een lijn in de file kan op 2 manieren geformatteerd zijn (afhankelijk of de types ook geraden zijn):
```
<naam>,<type>
<naam>
```
Bij de eerste keer dat we het spel opstarten, zal deze file leeg zijn, gezien we nog geen pokemon geraden hebben.

## Schrijven van de progress file
Om onze voortgang in het spel bij te houden, zullen we de gevonden info wegschrijven naar het progress bestand. Maak een methode `write_progress` op de `Pokedex` klasse, dewelke de Pokedex info gaat wegschrijven in een opgegeven bestand. Uiteraard mag enkel de info die de speler al geraden heeft weggeschreven worden.

```python
pokedex.write_progress("progress.txt")
```
Wat resulteert in een bestand `progress.txt` dat de volgende inhoud heeft:
```
Bulbasaur,Grass-Poison
Pidgey,Normal-Flying
Rattata,
Raticate,
Spearow,Normal-Flying
```

### Het lezen van de Progress data
Nu moeten we ook nog een een functie `read_progress_data` schrijven die zo'n bestand kan lezen en die een lijst teruggeeft met alle gevonden data. De functie geeft een lijst van tuples terug, waar elke tuple als volgt is opgesteld (nummer,type). Indien er geen types gevonden werden voor een lijn, wordt het None object meegegeven.

```python
>>> read_progress_data('progress.txt')
[('Bulbasaur', "Grass-Poison"),
 ('Pidgey', "Normal-Flying"),
 ('Rattata', None),
 ('Ratticate', None),
 ('Spearow', "Normal-Flying")]
```

## Alles bij elkaar brengen
Uiteindelijk gaan we alle voorgaande klassen en methodes combineren om ons spel te maken. Maak hiervoor een nieuwe functie `play_game` .

* Maak om te beginnen een nieuw `Pokedex` object aan
* Lees de Pokemon data vanuit het `pokemons.txt` bestand
  * Geef de output van deze functie door aan de Pokedex zodat er Pokemon worden toegevoegd
* Lees de Progress data vanuit het `progress.txt` bestand
  * Geef de output van deze functie door aan de Pokedex zodat de Progress Data wordt verwerkt

Nu moeten we tot slot nog de game logica ontwikkelen. Schrijf hiervoor een loop die zal blijven lopen zolang de gebruiker niet de code om te stoppen ingeeft. Zolang het spel loopt, heeft de gebruiker de mogelijkheid om:

* De naam en eventueel het type van een pokemon te gokken
  * Roep hiervoor dan de desbetreffende methode van de Pokedex op
* Een overzicht te krijgen van de hele Pokedex
  * Roep hiervoor dan de desbetreffende methode van de Pokedex op
* Te stoppen
  * Zorg hier zeker dat de juiste methode van de Pokedex opgeroepen wordt om de progress weg te schrijven

Om je alvast wat op weg te helpen, krijg je hier al een deel van de code. Vul aan met de juiste functies zodat het spel als 1 geheel werkt.

```python
stop_game = False

    while not stop_game:
        choice = input("What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? ").strip().upper()

        if choice == "G":
            # Vraag de speler om de naam van een pokemon in te geven
            # Vraag de speler om het type van de pokemon in te geven (de speler kan deze leeg laten als hij geen type wil gokken)
            # Valideer of dit een geldige pokemon is
            # Geef de juiste feedback terug aan de gebruiker

        elif choice == "S":
            # Print het overzicht van de huidige pokedex

        elif choice == "Q":
            # Stop de game
            # Schrijf de vooruitgang weg naar de progress fle

        else:
            # Laat de gebruiker weten dat het geen geldige keuze was
```

Als alles goed gecodeerd is, heb je nu een werkend spel, waarbij het de bedoeling is om alle 151 originele Pokemon te raden, met hun bijhorende type. Ben jij de Pokemon-expert en kan jij ze allemaal raden?
