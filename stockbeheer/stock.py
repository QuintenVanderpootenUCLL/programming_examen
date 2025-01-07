class Part():
    def __init__(self, partname, price):
        self.name = partname
        self.price = price
        self.__quantity = 0
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, amount):
        self.__quantity = amount
        if self.__quantity < 0:
            raise ValueError(f"Quantity for part {self.name} can't be negative")
    
    def info(self):
        return(f"{self.name}: Price = {self.price}, Available Quantity = {self.quantity}")
        

class Stock():
    def __init__(self):
        self.parts = {}
    
    def add_part(self, part_name, part_price, part_quantity):
        part_exists = self.parts.get(part_name, False)
        if part_exists:
            raise ValueError(f"Part with name {part_name} already exists in our stock")
        self.parts[part_name] = Part(part_name, part_price)
        self.parts[part_name].quantity = part_quantity

    def get_part(self, naam):
        return self.parts[naam]


    def remove_part(self, naam):
        self.parts.pop(naam)
    
    def restock_part(self, naam, amount):
        self.parts[naam].quantity += amount



class Shop():
    def __init__(self, naam):
        self.name = naam
        self.__stock = Stock()

    @property
    def stock(self):
        return self.__stock
    
    def load_stock_from_file(self):
        with open("stock.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip("\n").split("|")
            naam, prijs, amount = line
            self.stock.add_part(naam, float(prijs), int(amount))


    def save_stock_to_file(self):
        full_file = ""
        for item in self.stock.parts.values():
            full_file += f"{item.name}|{item.price}|{item.quantity}\n"
        with open("stock.txt", "w", encoding="utf-8") as file:
            file.write(full_file)
    

    def display_stock(self):
        result = ""
        result += "Current stock is:\n"
        for item in self.stock.parts.values():
            result += f"{item.name}: Price = {item.price}, Available Quantity = {item.quantity}\n"
        return result


    def register_sale(self, name, quantity_sold):
        part = self.stock.get_part(name)
        part.quantity -= quantity_sold
        with open("sales.txt", "a", encoding="utf-8") as file:
            file.write(f"Sold {quantity_sold} item(s) from {name} for price {part.price}\n")
        


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
            naam = input("What is the name of your new part? ")
            prijs = float(input("What is the price of this part? "))
            quantity = int(input("How much of this new part do u want to add to our stock? "))
            shop.stock.add_part(naam, prijs, quantity)
        elif choice == '2':
            # Restock existing part
            # Hier moet je code voorzien om aan de gebruiker te vragen voor welk onderdeel hij stuks wil toevoegen. Je moet hem ook nog vragen over hoeveel extra stuks het gaat
            # Met deze info kan de gebruiker de restock doen van het onderdeel uit de stock van onze shop
            naam = input("What is the name of the part u want to restock? ")
            quantity = int(input("What is the amount of parts u wanna add to our stock? "))
            shop.stock.restock_part(naam, quantity)
        elif choice == '3':
            # Register Sale
            # Hier moet je aan de gebruiker vragen welk onderdeel verkocht werd en hoeveel stuks er de deur uitgingen.
            # Met deze info kan je dan een verkoop registreren op de stock van onze shop
            naam = input("What is the name of the part u sold? ")
            amount = int(input("What is the amount of that you have sold? "))
            shop.register_sale(naam, amount)
        elif choice == '4':
            # Display Stock
            # Hier moet je code voorzien om de huidige stock van onze shop te tonen aan de gebruiker
            print(shop.display_stock())
        elif choice == '5':
            # Remove part from the stock
            # Hier vraag je de gebruiker de naam van het te verwijderen onderdeel
            # Met deze info verwijder je dan het volledige product uit de stock, zodat dit onderdeel niet langer in onze stocklijst voorkomt
            naam = input("What is the name of the part u want to remove from stock? ")
            shop.stock.remove_part(naam)
        elif choice == '6':
            # Stop and save
            # Met deze optie stoppen we de applicatie
            # Maar voor we stoppen, moeten we er nog voor zorgen dat we de huidige stockvoorraad opslaan in onze stock.txt file
            shop.save_stock_to_file()
            stop = True
        else:
            print("Invalid choice. Please try again.")

main()
