class Einkaufsliste:

    def __init__(self):
        self.__shoppingList = []

    def add_item(self):
        item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
        self.__shoppingList.append(item)
        print(f"Wurde der Liste hinzugefügt: {item}")

    def show_shopping_list(self):
        if len(self.__shoppingList) == 0:
            print("Deine Einkaufsliste ist leer")
        else:
            for item in self.__shoppingList:
                print(f"{item}")

    def start(self):
        while True:
            print("----- Einkaufsliste -----")
            print("1. Artikel zur Einkaufsliste hinzufügen")
            print("2. Einkaufsliste anzeigen")
            print("3. Programm beenden")

            select = input("Wähle bitte zwischen 1-3 aus:")
            match select:
                case "1":
                    self.add_item()
                case "2": 
                    self.show_shopping_list()
                case "3":
                    print("Programm wird beendet")
                    return
                case _:
                    print("Was war an 1-3 unverständlich?")