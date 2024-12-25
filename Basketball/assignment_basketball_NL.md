# Basketball

In deze oefening gaan we een python-script maken dat statistieken van een basketbalwedstrijd kan verwerken en dit zal omvormen naar wat men in de NBA een "box-score" noemt, oftewel een overzicht van de statistieken per speler. 

Op basis van twee bestanden, `match_data.txt`en `match_statistics.txt`, dewelke respectievelijk de ploegopstellingen en de wedstrijd gebeurtenissen bevatten, gaan we een nieuw bestand `output.txt` maken waarin we voor elke speler van de twee ploegen de statistieken zullen verzamelen.

## Class Player

Om te starten zullen we een klasse `Player` maken. Waneer we een `Player` object initialiseren, kunnen we een naam en nummer meegeven.

```python
>>> lbj = Player("Lebron James", 23)
>>> lbj.name
"Lebron James"
>>> lbj.number
23
```

Daarnaast willen we van elke speler een aantal statistieken gaan bijhouden
- Field Goals
  - FGA = Field Goal Attemps = Het aantal schoten (gescoord of gemist) dat een speler genomen heeft van binnen de 3-punt lijn
  - FGM = Field Goals Made = Het aantal schoten dat een speler gescoord heeft van binnen de 3-punt lijn
- Free Throws
  - FTA = Free Throw Attemps = Het aantal schoten (gescoord of gemist) dat een speler genomen heeft van aan de vrijworplijn
  - FTM = Free Throws Made = Het aantal schoten dat een speler gescoord heeft van aan de vrijworplijn
- 3 Points
  - 3PA = 3 Point Attemps = Het aantal schoten (gescoord of gemist) dat een speler genomen heeft van achter de 3-punt lijn
  - 3PM = 3 Points Made = Het aantal schoten dat een speler gescoord heeft van achter de 3-punt lijn
- Assists
  - AS = Assists = Het aantal passes dat een speler uitgedeeld heeft waarna een andere speler scoorde
- Rebounds
  - RB = Rebounds = Het aantal ballen dat een speler opgeraapt heeft na een misser

Initieel worden al deze statistieken geïnitialiseerd op 0.

Het moet ook mogelijk zijn om de statistieken op te vragen. Hiervoor schrijven we een property `statistics`, die alle statistieken van een speler zal teruggeven.

```python
>>> stats = lbj.statistics
>>> stats["FGA"]
0
>>> stats["FGM"]
0
>>> stats["FTA"]
0
>>> stats["FTM"]
0
>>> stats["3PA"]
0
>>> stats["3PM"]
0
>>> stats["AS"]
0
>>> stats["RB"]
0
```

### Statistieken toevoegen aan een speler
Nu willen we het mogelijk maken om statistieken toe te voegen aan onze speler. Om dit te bereiken zullen we methodes aanmaken die opgeroepen kunnen worden om bepaalde statistieken aan te passen.

Maak om te beginnen een methode `add_FG` aan dewelke 1 parameter ontvangt om aan te geven of de field goal gescoord werd. Pas op basis hiervan de juiste statistiek(en) aan van de speler.

Voorzie gelijkaardige methodes voor de 4 andere categorieën van statistieken.

```python
>>> lbj.add_FG("Scored")
>>> lbj.add_FG("Missed")
>>> stats["FGA"]
2
>>> stats["FGM"]
1
>>> lbj.add_FT("Scored")
>>> stats["FTA"]
1
>>> stats["FTM"]
1
>>> lbj.add_AS()
>>> stats["AS"]
1
etc...
```

## Class Team
Vervolgens willen we een Team kunnen aanmaken om alle spelers in op te slaan. Om dit te bereiken, zullen we een klasse `Team` maken. Wanneer we een object van deze klasse maken, specifiëren we twee argumenten: een teamnaam en de afkorting van de teamnaam.

```python
>>> lakers = Team("LA Lakers", "LAL")
>>> lakers.name
"LA Lakers"
>>> lakers.abbreviation
"LAL"
```

### Toevoegen en ophalen van spelers
Om later iets nuttig te kunnen doen met ons team, moeten we eerst spelers kunnen toevoegen aan het team. Maak hiervoor een methode `add_player`, die als argumenten een spelersnaam en spelersnummer krijgt en daarmee een `Player` aanmaakt en toevoegt aan ons team.

```python
>>> lakers.add_player("Lebron James", 23)
```

Om het resultaat van deze methode te zien, moeten we ook een methode `get_player` voorzien. Deze methode ontvangt een spelersnummer als argument en op basis daarvan geeft hij het `Player` object terug dat binnen dit team daarmee gelinked is.

```python
>>> lbj = lakers.get_player(23)
>>> lbj.name
"Lebron James"
>>> lbj.number
23
```

### Toon alle spelers van een team
Het is ook mogelijk om aan onze klasse `Team` te vragen welke `Players`  er tot dit team behoren:

```python
>>> lakers.players
dict_values([<main.Player object at 0x10a4dd1d0>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin de speler:
# [Player("Lebron James")]
>>> lakers.add_player("Anthony Davis", 3)
>>> lakers.players
dict_values([<main.Player object at 0x10a4dd1d0>, <main.Player object at 0x10a405e00>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin de twee spelers:
# [Player("Lebron James"), Player("Anthony Davis")]
```

## Class Match
Om alle informatie rond een match te verzamelen, zullen we een klasse `Match` maken. Bij het aanmaken van een `Match` object, moet er geen parameter meegegeven worden.

```python
>>> match = Match()
```

### Toevoegen van de match data
In deze folder vind je een file met de match data: `match_data.txt`, dewelke informatie bevat over de twee ploegen die gespeeld hebben, alsook alle spelers die voor een van beide ploegen op het terrein stonden. Er zijn twee mogelijke soorten lijnen die kunnen voorkomen:

```
# Lijn die een team bepaalt
TEAM - <team_name> - <team_abbreviation>
# Lijn die een speler voorstelt
#<player_number> - <player_name>
```

De match_data file is steeds hetzelfde opgebouwd. Voor elke ploeg heb je eerst een lijn die het team bepaalt, gevolgd door x-aantal lijnen die de spelers van dat team voorstellen. 

(Bekijk zeker de file om het formaat beter te begrijpen)

Voeg een methode read_match_data_file toe aan de `Match`  klasse. Deze methode leest de data uit de file in, maakt de spelers aan en creëert de twee `Teams` met deze `Players`.

Schrijf de logica zo dat de file volledig ingelezen wordt, de data lijn per lijn wordt verwerkt en dat op het einde ons `Match` object twee `Teams` bevat, met elk de nodige `Player` objecten.

```python
>>> match.read_match_data_file("match_data.txt")
```

### Opvragen van een team
Om het resultaat van de vorige methode te zien, moeten we ook een methode `get_team` voorzien. Deze methode ontvangt een teamafkorting als argument en op basis daarvan geeft hij het `Team` object terug dat binnen deze match daarmee gelinked is.

```python
>>> team = match.get_team("LAL")
>>> team.name
"LA Lakers"
```

### Toon alle teams uit een match
We zullen ook een property `teams` voorzien in `Match`, dewelke een lijst teruggeeft van alle teams die behoren tot deze match.

```python
>>> match.teams
dict_values([<main.Team object at 0x10a4dd1d0>, <main.Team object at 0x10a405e00>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin de twee teams:
#[Team("LAL"), Team("SAS")] 
```

### Toevoegen van de statistieken
In deze folder vind je een file met de statistieken: `match_statistics.txt`, dewelke informatie bevat over de acties van een speler tijdens de match. Er zijn twee mogelijke soorten lijnen die kunnen voorkomen:

```
# Lijn voor een FG, FT of 3P
<team_abbreviation>,#<player_number>,<type>,<scored/missed>
# Lijn voor een AS of RB
<team_abbreviation>,#<player_number>,<type>
```
(Bekijk zeker de file om het formaat beter te begrijpen)

Schrijf nu een methode `read_match_statistics_file` op onze `Match` klasse. Deze methode zal alle data uit onze file inlezen en de respectievelijke statistieken voor de juiste speler aanpassen.

```python
>>> match.read_match_statistics_file("match_statistics.txt")
```

### Tonen van de match statistieken
Nu dat we alle statistieken hebben ingeladen in onze match, kunnen we onze "box-score" gaan aanmaken, zodat we kunnen zien hoe al onze spelers gepresteerd hebben.

Maak een methode `display_match` die een string teruggeeft met alle statistieken van de spelers en die er zo uit ziet:

```python
>>> print(match.display_match())
------------------------------------------------------------------------------------
| LA Lakers                                                                        |
------------------------------------------------------------------------------------
| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |
| #23 | Lebron James                 | 3   | 2   | 0   | 0   | 2   | 1   | 5  | 2  |
| #28 | Rui Hachimura                | 2   | 0   | 4   | 2   | 4   | 1   | 1  | 4  |
| #3  | Anthony Davis                | 2   | 2   | 3   | 2   | 2   | 2   | 1  | 4  |
| #4  | Dalton Knecht                | 3   | 3   | 4   | 3   | 1   | 1   | 1  | 2  |
| #15 | Austin Reaves                | 2   | 2   | 3   | 2   | 2   | 2   | 3  | 1  |
| #1  | D'Angelo Russell             | 3   | 2   | 6   | 4   | 2   | 1   | 8  | 2  |
| #12 | Max Christie                 | 3   | 2   | 0   | 0   | 5   | 3   | 0  | 0  |
| #5  | Cam Reddish                  | 3   | 3   | 3   | 3   | 2   | 0   | 5  | 1  |
| #10 | Christian Koloko             | 2   | 2   | 1   | 0   | 2   | 0   | 3  | 4  |
| #7  | Gabe Vincent                 | 1   | 0   | 2   | 1   | 0   | 0   | 3  | 1  |
| #20 | Maxwell Lewis                | 3   | 2   | 4   | 3   | 2   | 0   | 1  | 1  |
| #94 | Amel Traore                  | 1   | 1   | 3   | 0   | 2   | 0   | 6  | 2  |
------------------------------------------------------------------------------------
| San Antonio Spurs                                                                |
------------------------------------------------------------------------------------
| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |
| #40 | Harrison Barnes              | 1   | 0   | 1   | 0   | 4   | 0   | 3  | 2  |
| #30 | Julian Champagnie            | 3   | 2   | 2   | 0   | 1   | 1   | 1  | 4  |
| #1  | Victor Wembanyama            | 4   | 2   | 0   | 0   | 1   | 0   | 2  | 2  |
| #5  | Stephon Castle               | 2   | 1   | 2   | 1   | 2   | 1   | 1  | 3  |
| #3  | Chris Paul                   | 0   | 0   | 1   | 1   | 3   | 0   | 2  | 1  |
| #0  | Keldon Johnson               | 1   | 0   | 1   | 0   | 2   | 2   | 1  | 2  |
| #24 | Devin Vassell                | 3   | 1   | 0   | 0   | 3   | 0   | 0  | 2  |
| #33 | Tre Jones                    | 2   | 1   | 5   | 1   | 2   | 1   | 2  | 3  |
| #23 | Zach Collins                 | 2   | 0   | 4   | 1   | 3   | 1   | 4  | 1  |
| #14 | Blake Wesley                 | 2   | 1   | 0   | 0   | 3   | 3   | 2  | 2  |
| #28 | Charles Bassey               | 4   | 3   | 2   | 2   | 8   | 6   | 3  | 2  |
| #22 | Malaki Branham               | 3   | 1   | 2   | 2   | 4   | 3   | 0  | 1  |
| #25 | Sidy Cissoko                 | 3   | 3   | 2   | 2   | 2   | 0   | 1  | 2  |
| #54 | Sandro Mamukelashvili        | 3   | 1   | 3   | 2   | 4   | 2   | 1  | 2  |
------------------------------------------------------------------------------------
```

## Wegschrijven van de statistieken naar een bestand
We willen onze statistieken ook kunnen wegschrijven naar een bestand. Maak hiervoor een methode `write_match_details` aan op de match klasse, dewelke onze match_details zal wegschrijven naar een opgegeven file:


```python
match.write_match_details("output.txt")
```
Dit resulteert in een file `output.txt` met de volgende inhoud:
```
------------------------------------------------------------------------------------
| LA Lakers                                                                        |
------------------------------------------------------------------------------------
| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |
| #23 | Lebron James                 | 3   | 2   | 0   | 0   | 2   | 1   | 5  | 2  |
...
| #94 | Amel Traore                  | 1   | 1   | 3   | 0   | 2   | 0   | 6  | 2  |
------------------------------------------------------------------------------------
| San Antonio Spurs                                                                |
------------------------------------------------------------------------------------
| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |
| #40 | Harrison Barnes              | 1   | 0   | 1   | 0   | 4   | 0   | 3  | 2  |
...
| #54 | Sandro Mamukelashvili        | 3   | 1   | 3   | 2   | 4   | 2   | 1  | 2  |
------------------------------------------------------------------------------------

```
(Merk op dat de inhoud van deze file hetzelfde is als de output van `display_match`)

## Alles samen brengen
We hebben nu alle stukjes in handen om van een bepaalde match alle statistieken te gaan berekenen en weg te schrijven naar een file. Roep alle aangemaakte functies op en bewonder het resultaat!


```python
>>> match = Match()
>>> match.read_match_data_file("match_data.txt")
>>> match.read_match_statistics_file("match_statistics.txt")
>>> match.write_match_details("output.txt")
```
Dit zou moeten resulteren in een file `output.txt` 
