from db_context import DBContext as dbc
class ItemDBContext:
    
    def __init__(self):
        self.db_context = dbc("shoppinglist.db")
        self.create_item_table()
        
    def create_item_table(self):
        # Erstellt die Datenbank Students
        create_table = """
        CREATE TABLE IF NOT EXISTS Items
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(64) NOT NULL,
            amount INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """
        self.db_context.create_database(create_table)
    
    # C - Create - INSERT
    def create_item(self, item:tuple):
        print(item)
        self.db_context.execute(f"""
                                INSERT INTO Items (name, price, amount)
                                values
                                ('{item[0]}',{item[1]},{item[2]});
                                """)
    # R - Read - SELECT
    def get_all_items(self):
        return self.db_context.execute(f"""
                                        SELECT * FROM Items;
                                        """)
        
    def get_item_by_id(self, id:int):
        return self.db_context.execute(f"""
                                        SELECT * FROM Items WHERE id = {id};
                                        """)
    
    # U - Update - UPDATE
    def update_item(self, id:int, _name:str="", _price:float=0, _amount:int=0):
        result = self.get_item_by_id(id)
        
        if len(result) == 0:
            return
        
        name = _name
        price = _price
        amount = _amount
        
        if name == "":
            name = result[0][0]
        if price == 0:
            price = result[0][1]
        if amount == 0:
            amount = result[0][2]
            
        self.db_context.execute(f"UPDATE ITEMS SET name = '{name}', price = {price}, amount = {amount} where id = {id}")
            
    # D - Delete - DELETE
    def delete_item(self, id:int):
        result = self.get_item_by_id(id)
        
        if len(result) == 0:
            return
        
        self.db_context.execute(f"DELETE FROM Items where id = {id}")
        
        