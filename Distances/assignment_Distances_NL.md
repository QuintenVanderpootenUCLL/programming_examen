
# Examenvraag : Afstanden

We runnen een dierenpark in Zuid-Afrika waar een heel aantal dieren in ons park rondlopen. We willen graag informatie verzamelen over de afstanden die onze dieren per dag afleggen en ook willen we weten of er bepaalde roofdieren op een bepaald moment in de buurt van een prooidier zijn geweest.

Jouw opdracht is om een Python-programma te schrijven dat de locatiegegevens van de dieren analyseert en de nodige berekeningen gaat doen. De resultaten van onze analyse zullen we dan wegschrijven naar een file.

## animals.txt

Het bestand animals.txt bevat de lijst van onze dieren. Elk dier heeft bij ons een unieke naam en behoort tot een soort van dieren. Het formaat van de file is als volgt:

```
<naam dier>,<soort dier>
```

Bekijk zeker de file om het formaat beter te begrijpen.

Maak een functie die op basis van een bestandsnaam het bestand gaat inlezen. Elke rij uit het bestand zal dan verwerkt worden en opgeslagen in een passende collectie. Als het hele bestand ingelezen is, zal deze functie de collectie teruggeven.

Om deze functie te testen, kan je gebruik maken van het bestand `sample_animals.txt`.

```python
>>> read_animal_data("sample_animals.txt")
{'Leo': 'Lion', 'Stripes': 'Tiger', 'Zigzag': 'Zebra', 'Bananas': 'Monkey'}
```

## locations.txt

Het bestand locations.txt bevat de lijst van locaties van de voorbije dag. Voor elk van onze dieren zijn er 24 registraties (voor elk uur 1 registratie). 

Een registratie wordt gekenmerkt door een X en Y coördinaat. Voor de eenvoudigheid stellen we dat een coördinaat voorgesteld wordt door een geheel getal tussen 0 en 100.

Het formaat van 1 registratie is als volgt:

```
<tijdstip>,<naam dier>,<X>,<Y>
```

Bekijk zeker de file om het formaat beter te begrijpen.

Maak een functie die op basis van een bestandsnaam het bestand gaat inlezen. Elke rij uit het bestand zal dan verwerkt worden en opgeslagen in een passende collectie. Als het hele bestand ingelezen is, zal deze functie de collectie teruggeven.

Om deze functie te testen, kan je gebruik maken van het bestand `sample_locations.txt`.

```python
>>> read_location_data("sample_locations.txt")
{'Leo': [('00:00', 13, 42), ('08:00', 86, 8), ('16:00', 78, 14), ('22:00', 64, 0)], 'Stripes': [('00:00', 63, 45), ('08:00', 61, 67), ('16:00', 61, 66), ('22:00', 73, 36)], 'Zigzag': [('00:00', 23, 77), ('08:00', 87, 7), ('16:00', 28, 0), ('22:00', 52, 41)], 'Bananas': [('00:00', 60, 73), ('08:00', 82, 87), ('16:00', 61, 66), ('22:00', 45, 90)]}
```

## Totaal afgelegde afstand

Voor elk dier hebben we een overzicht van alle coördinaten per uur. Schrijf nu een functie die gaat berekenen hoeveel afstand een dier heeft afgelegd in 24 uur. Om dit te berekenen moet je de afstand optellen die het dier elk uur aflegt. 

Om de afstand tussen twee coördinaten te berekenen, kan je gebruik maken van de formule die we ook in de oefeningen gezien hebben:

$$
\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

Het resultaat dat je hier uitkomt, stelt de afstand in kilometer voor dat het dier die dag heeft afgelegd.

```python
>>> calculate_travelled_distance(location_data["Leo"])
110.3284875743763
```

## Meest actieve dier

Schrijf een functie die gaat berekenen welk van onze dieren het meest actief was tijdens de voorbije dag. Gebruik hiervoor de functie die we zonet hebben aangemaakt en waarmee we de totale afgelegde afstand kunnen berekenen. 

De functie geeft het meest actieve dier terug (= het dier met de grootste totale afstand), alsook de totaal afgelegde afstand van dat dier.

```python
>>> most_active, active_distance = most_active_animal(location_data)
>>> print(f"Most active animal: {most_active} with distance {active_distance:.2f}")
"Most active animal: Zigzag with distance 201.77"
```

## Meest luie dier

Schrijf een functie die gaat berekenen welk van onze dieren het meest lui was tijdens de voorbije dag. Gebruik hiervoor de functie die we zonet hebben aangemaakt en waarmee we de totale afgelegde afstand kunnen berekenen. 

De functie geeft het meest luie dier terug (= het dier met de kleinste totale afstand), alsook de totaal afgelegde afstand van dat dier.

```python
>>> most_lazy, lazy_distance = most_lazy_animal(location_data)
>>> print(f"Most lazy animal: {most_lazy}with distance {lazy_distance:.2f}")
"Most lazy animal: Stripes with distance 55.40"
```

## Ontmoetingen tussen roof- en prooidier

We willen een functie `flag_predator_prey_contact` maken die voor elk tijdstip gaat kijken of er dieren in elkaars buurt geweest zijn, en meer bepaald of er een roofdier binnen de 2km gekomen is van een prooidier.

Om te beginnen moet je dus ergens bijhouden of een soort dier een roofdier of een prooidier is. Dit kan je doen door voor elke gekende diersoort uit het animals.txt bestand ergens bij te houden of het een roofdier (predator) of prooidier (prey) is. Dit mag hardcoded gebeuren in het begin van de functie.

Daarna zal je al de locatiedata die we verzameld hebben, moeten groeperen zodat we er later berekeningen op kunnen doen. Je wilt per tijdstip weten waar elk dier op dat ogenblik was.

Gebruik deze data om per tijdstip te kijken of er een contact geweest is tussen een roofdier (predator) en prooidier (prey). Verifieer elke mogelijke combinatie van dieren, en bereken de afstand tussen de twee dieren door gebruik te maken van dezelfde formule om afstanden te berekenen die we al eerder gebruikten.

Indien twee dieren zich op 2 km of minder van elkaar bevinden, en het betreft hier een roof- en prooidier, schrijf deze informatie dan weg naar een nieuwe file.

Als resultaat van deze functie hebben we een nieuwe file contacts.txt, waarbij we voor elke ontmoeting een lijn hebben in het volgende formaat:

```
Time <tijdstip>, <naam1> (<soort1>), <naam2> (<soort2>), Distance <afstand>
```

```python
>>> flag_predator_prey_contact(location_data, animal_data)
```
Wat resulteert in een bestand contacts.txt dat de volgende inhoud heeft:

```
Time 08:00, Leo (Lion), Zigzag (Zebra), Distance 1.41
Time 16:00, Stripes (Tiger), Bananas (Monkey), Distance 0.00
```

## Alles nu samen brengen

Tot slot gaan we nu alle functies die we eerder geschreven hebben, bij elkaar brengen. Als alles goed gecodeerd is, krijgen we dan de verwachte feedback te zien over het meest actieve dier, het meest luie dier en de ontmoetingen tussen roof- en prooidieren.

We kunnen nu ook gebruik maken van de volledige bestanden.

```python
>>> animal_data = read_animal_data("animals.txt")
>>> location_data = read_location_data("locations.txt")

>>> most_active, active_distance = most_active_animal(location_data)
>>> print(f"Most active animal: {most_active} with distance {active_distance:.2f}")
"Most active animal: Gallop with distance 1548.18"

>>> most_lazy, lazy_distance = most_lazy_animal(location_data)
>>> print(f"Most lazy animal: {most_lazy}with distance {lazy_distance:.2f}")
"Most lazy animal: Tower with distance 971.62"

>>> flag_predator_prey_contact(location_data, animal_data)
>>> print("Contacts between predators and prey are saved in 'contacts.txt'.")
```

Waarbij de contacts.txt er als volgt zou moeten uitzien:

```
Time 00:00, Viper (Snake), Rarity (Zebra), Distance 1.41
Time 01:00, Roar (Lion), Strider (Zebra), Distance 1.41
Time 01:00, Paws (Bear), Stripey (Zebra), Distance 1.41
Time 01:00, Ember (Tiger), Clover (Cow), Distance 1.41
Time 01:00, Ember (Tiger), Necky (Giraffe), Distance 1.41
(etc)
```