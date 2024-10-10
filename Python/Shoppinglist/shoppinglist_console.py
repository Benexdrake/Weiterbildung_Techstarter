from item_db_context import ItemDBContext as idc

class ShoppinglistConsole:
    def __init__(self):
        self.item_db = idc()

    def add_item(self):
        try:
            name = input("What is the Name of the Item: ")
            price_input = input("Enter a Price: ")
            price = float(price_input)
            amount_input = input("Enter how much u need: ")
            amount = int(amount_input)
            
            self.item_db.create_item((name,price,amount))
            print("Item added to Shoppinglist")
        except:
            print("Please enter a Number as ID, return to main menu...")


    def show_shopping_list(self):
        shopping_list = self.item_db.get_all_items()
        if len(shopping_list) == 0:
            print("Deine Einkaufsliste ist leer")
        else:
            for item in shopping_list:
                print(f"{item}")
    
    
    def update_item(self):
        try:
            id = int(input("Please enter a id: "))
            name = input("What is the Name of the Item: ")
            price = float(input("Enter a Price: "))
            amount = int(input("Enter how much u nedd: "))
            
            
            
            self.item_db.update_item(id,name,price,amount)
        except:
            print("Please enter a Number as ID, return to main menu...")
        
        
    def delete_item(self):
        try:
            id = int(input("Please enter a id: "))
            self.item_db.delete_item(id)
        except:
            print("Please enter a Number as ID, return to main menu...")
            

    def start(self):
        while True:
            print("----- Einkaufsliste -----")
            print("1. Add Item to Shoppinglist")
            print("2. Show all Items from Shoppinglist")
            print("3. Update a Item from Shoppinglist")
            print("4. Delete a Item from Shoppinglist")
            print("5. Programm beenden")

            select = input("Wähle bitte zwischen 1-5 aus: ")
            match select:
                case "1":
                    self.add_item()
                case "2": 
                    self.show_shopping_list()
                case "3":
                    self.update_item()
                case "4":
                    self.delete_item()
                case "5":
                    print("Programm wird beendet")
                    return
                case _:
                    print("Was war an 1-5 unverständlich?")