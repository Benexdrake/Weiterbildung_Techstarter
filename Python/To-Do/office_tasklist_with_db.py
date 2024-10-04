import datetime
import sqlite3

class OfficeTasklist_DB:
    
    def __init__(self):
        self.conn = sqlite3.connect('todo_list.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Todo
                            (  
                                id INTEGER PRIMARY KEY,
                                task varchar(128),
                                date DATE
                            );
                            ''')

    # Create
    def add_task(self):
        while True:
            task = input("Please enter a Task: ")
            if task:
                while True:
                    date_input = input("Please enter a Date in YYYY-MM-DD format: ")
                    try:
                        date_entered = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                        self.cursor.execute(f'''INSERT INTO todo (task, date) VALUES ("{task}","{date_entered}")''')
                        self.conn.commit()
                        return
                    except:
                        print("Please enter a real Date")

    # Read            
    def show_tasklist(self):
        self.cursor.execute("SELECT * FROM todo")
        results = self.cursor.fetchall()
        if len(results) == 0:
            print("Nothing to see here!")
        else:
            pass
            for todo in results:
                print(f'ID: {todo[0]}\t| Task: {todo[1]}\t | Date: {todo[2]}')
        print("")
    
    
    # Update
    
    # Delete
    
    def start(self):
        while True:
            print("1. Create Task")
            print("2. Show all Tasks")
            print("3. Exit")
            choice = input("Please enter 1,2 or 3: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasklist()
            elif choice == "3":
                self.conn.close()
                return
            else:
                print("Error, wrong Choice, please enter again!")