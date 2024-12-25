# Examenvraag: Stockbeheer

Jullie zijn de trotse zaakvoerders van een IT-shop waar mensen pc-onderdelen kunnen kopen. Om een overzicht te kunnen houden over de stock van jouw winkel, besluit je een python-script te schrijven. Met deze applicatie kan je voor elk onderdeel bijhouden hoeveel items we nog in voorraad hebben, alsook dewelke we verkocht hebben voor een bepaalde prijs.

## Onderdelen

Maar first things first, we gaan onze applicatie deel per deel opbouwen. Om te beginnen gaan we alvast een klasse `Part` aanmaken. Een `Part` stelt een computeronderdeel voor dat we verkopen in onze IT-shop. Een `Part` heeft een naam, een prijs en de hoeveelheid items die we hiervan in stock hebben. Bij het aanmaken van een `Part` wordt de hoeveelheid standaard op 0 gezet.

```python
>>> part = Part("Corsair 32GB DDR-5",114.90)
>>> part.name
"Corsair 32GB DDR-5"
>>> part.price
114.90
>>> part.quantity
0
>>> part.quantity = 20
>>> part.quantity
20
```

Wanneer we de hoeveelheid van een `Part` willen aanpassen, moeten we checken dat het aantal niet onder 0 gaat. We willen natuurlijk geen onderdelen verkopen die we niet in onze stock hebben!

```python
>>> part.quantity = -1
ValueError("Quantity for part Corsair 32GB DDR-5 can't be negative")
```

Tot slot voorzien we ook nog een methode om een string-representatie te tonen van ons `Part` object. Deze methode zal de naam, de prijs en de hoeveelheid in een geformatteerde structuur terug geven:

```python
>>> part.info()
"Corsair 32GB DDR-5: Price = 114.90, Available Quantity = 20"
```

## Stock

Nu we een klasse gemaakt hebben om onze onderdelen voor te stellen, is het tijd voor een volgende stap. Maak een klasse `Stock` aan, die gebruikt zal worden om al onze onderdelen die we verkopen in onze shop, bij te houden.

Bij de aanmaak van een object voor de `Stock` klasse moeten er geen parameters meegegeven worden.

```python
>>> stock = Stock()
```

### Toevoegen van onderdelen aan onze stock

Uiteraard moeten we onderdelen (`Part`) kunnen toevoegen aan onze stock. Maak hiervoor een methode `add_part` aan op onze `Stock` klasse. Deze methode neemt de naam, prijs en hoeveelheid van een onderdeel als argument en zal als resultaat een `Part` object toevoegen aan onze stock. 

Om onze stock voor te stellen, willen we gebruik maken van een collectie waar we later makkelijk een onderdeel op basis van een naam kunnen opzoeken, zonder dat we over heel de collectie moeten itereren. 

```python
>>> stock.add_part("Corsair 32GB DDR-5",114.90, 20)
>>> stock.add_part("WD Red Plus 12TB",289.00,6)
```

Het is natuurlijk niet mogelijk om een `Part` object toe te voegen als er al een onderdeel in onze stock zit met dezelfde naam.

```python
>>> stock.add_part("WD Red Plus 12TB",289.00,6)
ValueError("Part with name WD Red Plus 12TB already exists in our stock")
```

Om het resultaat van de bovenstaande methode te kunnen zien, moeten we ook een extra methode `get_part` voorzien. Deze methode ontvangt een naam van een onderdeel als argument en op basis daarvan geeft die het corresponderende `Part` object uit onze stock terug.

```python
>>> part = stock.get_part("WD Red Plus 12TB")
>>> part.name
"WD Red Plus 12TB"
```

### Toon alle onderdelen uit onze stock

Verder zullen we ook een property `parts` voorzien op ons `Stock` object. Deze property zal alle onderdelen uit onze stock teruggeven in een lijst.

```python
>>> stock.parts
dict_values([<__main__.Part object at 0x1010ff230>, <__main__.Part object at 0x101244e10>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin de twee onderdelen:
# [Part("Corsair 32GB DDR-5"),Part("WD Red Plus 12TB")]
```

### Verwijderen van onderdelen uit de stock

Het moet ook mogelijk zijn om bepaalde onderdelen helemaal uit de stock te halen. Voorzie hiervoor een methode `remove_part`, die op basis van de naam van het onderdeel, dit specifieke onderdeel uit de stock haalt.

```python
>>> stock.parts
dict_values([<__main__.Part object at 0x1010ff230>, <__main__.Part object at 0x101244e10>])
>>> stock.remove_part("WD Red Plus 12TB")
>>> stock.parts
dict_values([<__main__.Part object at 0x1010ff230>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin het onderdeel:
# [Part("Corsair 32GB DDR-5")]
```

### Aanpassen van de stock voor een onderdeel

We kunnen ook extra hoeveelheden van een bepaald onderdeel toevoegen. Om dit te doen, voorzien we een methode `restock_part`. Deze methode ontvangt de naam van een bestaand onderdeel, alsook het aantal stuks dat we willen toevoegen aan de bestaande hoeveelheid.

```python
>>> part = stock.get_part("WD Red Plus 12TB")
>>> part.quantity
10
>>> stock.restock_part("WD Red Plus 12TB", 5)
>>> part.quantity
15
```

## Klasse Shop

Maak ook een klasse `Shop` aan. De constructor van deze klasse neemt 1 argument aan: De naam van onze shop. Bij het aanmaken van een shop, maken we ook meteen een `Stock` object aan, dat we bewaren in een private field.

```python
>>> shop = Shop("The IT Shop")
>>> shop.name
"The IT Shop"
```

Om aan onze private field stock te kunnen, voorzien we ook een property `stock`:

```python
>>> shop.stock
```

### Inladen van stock vanuit file

Onze huidige stock is opgeslagen in een bestand `stock.txt`. Elke aparte lijn stelt een ander onderdeel uit onze stock voor. Het formaat voor elke lijn is steeds hetzelfde:

```
<onderdeel_naam>|<onderdeel_prijs>|<onderdeel_hoeveelheid>
```

(Bekijk zeker de file om het formaat beter te begrijpen)

Schrijf nu een methode `load_stock_from_file` op onze `Shop` klasse, die onze stockfile gaat inlezen en voor elke gevonden lijn een onderdeel gaat toevoegen aan onze stock. Gebruik hiervoor de `add_part` methode die we eerder gemaakt hebben.

```python
>>> shop.load_stock_from_file()
>>> shop.stock.parts
dict_values([<__main__.Part object at 0x1010ff230>, <__main__.Part object at 0x101244e10>])
# Let op, bij jouw output kan de geheugenlocatie verschillend zijn, maar voor het overige zou je de output moeten herkennen
# Als we even abstractie maken van de effectieve output, komt het er eigenlijk op neer dat we een lijst krijgen met daarin de twee onderdelen:
# [Part("Corsair 32GB DDR-5"),Part("WD Red Plus 12TB")]
```

### Wegschrijven van de nieuwe stocksituatie in een file

Het moet mogelijk zijn om de nieuwe stockstatus weg te schrijven naar de `stock.txt` file. Voorzie hiervoor een methode `save_stock_to_file` op de klasse `Shop`. Deze methode zal de inhoud van onze stock wegschrijven naar de opgegeven file. Hou bij het wegschrijven rekening met het formaat van een lijn zoals we gezien hebben bij het inlezen van de file in het vorige hoofdstuk!

```python
>>> shop.save_stock_to_file()
```

Bovenstaande methode resulteert in een `stock.txt` die er zo kan uitzien:

```
Corsair 32GB DDR-5|114.90|20
Kingston Fury 64GB DDR-5|219.90|14
G.Skill 32GB DDR-5|117.50|18
AMD Ryzen 5 7600X|199.90|4
(etc)
```

### Tonen van de huidige stock

We willen ook de huidige stock kunnen tonen in onze terminal. Schrijf hiervoor de methode `display_stock`. Wanneer deze methode aangeroepen wordt, zal deze een string maken met daarin alle informatie over onze stock:

```python
>>> shop.display_stock()
'''Current stock is:
Corsair 32GB DDR-5: Price = 114.90, Available Quantity = 20
Kingston Fury 64GB DDR-5: Price = 219.90, Available Quantity = 14
G.Skill 32GB DDR-5: Price = 117.50, Available Quantity = 18
AMD Ryzen 5 7600X: Price = 199.90, Available Quantity = 4
Intel Core i5-2400: Price = 159.90, Available Quantity = 8
...'''
```

### Registreren van een verkoop

Willen we dat onze winkel winst blijft maken, moeten we natuurlijk ook af en toe een onderdeel kunnen verkopen! Maar belangrijk om te onthouden is dat wanneer we een onderdeel verkopen, we dit ook voor de belastingen moeten registeren. Anders riskeren we forse boetes op het einde van het jaar!

Maak een methode `register_sale` aan op de klasse `Shop`. Deze methode ontvangt de naam van het verkochte onderdeel, en het aantal stuks dat we aan de klant willen verkopen. Uiteraard zullen we eerst moeten checken of dit wel een onderdeel is dat we in onze stock hebben en als dit het geval is, moeten we ook nog zeker weten dat we nog genoeg stuks in onze voorraad hadden!

Als dit allemaal goed blijkt te zijn, dan kunnen we onze huidige voorraad verminderen met het aantal verkochte items.

```python
>>> shop.register_sale("Corsair 32GB DDR-5", 5)
# Als we nu opvragen hoeveel stuks we nog hebben van dit onderdeel, dan zal er 15 (20 - 5) getoond worden
```

Om ook de belastingen tevreden te houden, zal er op het einde van deze methode ook een lijn toegevoegd worden aan het `sales.txt` bestand. Hierin verzamelen we alle verkopen die ooit gebeurd zijn in onze winkel. Een voorbeeld van deze file ziet er als volgt uit:

```
Sold 1 item(s) from product GIGABYTE Radeon RX 7800 for price 499.00
Sold 2 item(s) from product Kingston Fury 64GB DDR-5 for price 219.90
(etc)
```

## Alles bij elkaar brengen

Nu we alle componenten gebouwd hebben om ons systeem te laten werken, is het de hoogste tijd om alles bij elkaar te brengen. Hiervoor gaan we een `main` methode maken die onze applicatie doet draaien. Maar voor we daaraan kunnen beginnen, moeten we nog een functie `display_menu` maken, die onze gebruiker het menu van onze applicatie toont. 

Gelukkig krijg je hiervoor de code al van ons. Kopieer de volgende functie in jouw script:

```
def display_menu():
    print("\n===== IT Store Stock Management System =====")
    print("1. Add new part")
    print("2. Restock existing part")
    print("3. Sell part")
    print("4. View stock")
    print("5. Remove existing part")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice
```

### De main-functie

Onze applicatie zal aangestuurd worden door de main-functie. Ook deze krijg je (gedeeltelijk) van ons. Kopieer de volgende code alvast in jouw script:

```
def main():
    shop = Shop("The IT Store")
    shop.load_stock_from_file()

    stop = False
    while not stop:
        choice = display_menu()

        if choice == '1':
            # Add new part
            # Hier moet je nog code voorzien om aan de gebruiker te vragen welk onderdeel hij wil aanmaken, wat de prijs is en wat de hoeveelheid stuks is die er zijn
            # Met deze informatie zal je dan een nieuw onderdeel aan de stock van onze shop kunnen toevoegen

        elif choice == '2':
            # Restock existing part
            # Hier moet je code voorzien om aan de gebruiker te vragen voor welk onderdeel hij stuks wil toevoegen. Je moet hem ook nog vragen over hoeveel extra stuks het gaat
            # Met deze info kan de gebruiker de restock doen van het onderdeel uit de stock van onze shop

        elif choice == '3':
            # Register Sale
            # Hier moet je aan de gebruiker vragen welk onderdeel verkocht werd en hoeveel stuks er de deur uitgingen.
            # Met deze info kan je dan een verkoop registreren op de stock van onze shop

        elif choice == '4':
            # Display Stock
            # Hier moet je code voorzien om de huidige stock van onze shop te tonen aan de gebruiker

        elif choice == '5':
            # Remove part from the stock
            # Hier vraag je de gebruiker de naam van het te verwijderen onderdeel
            # Met deze info verwijder je dan het volledige product uit de stock, zodat dit onderdeel niet langer in onze stocklijst voorkomt

        elif choice == '6':
            # Stop and save
            # Met deze optie stoppen we de applicatie
            # Maar voor we stoppen, moeten we er nog voor zorgen dat we de huidige stockvoorraad opslaan in onze stock.txt file

        else:
            print("Invalid choice. Please try again.")

main()

```

Zoals je ziet hebben we al veel prijs gegeven, maar ga je voor elke optie nog een deeltje code moeten toevoegen om de juiste methodes en properties op te roepen. Succes!