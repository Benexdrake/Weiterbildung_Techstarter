import datetime
import os
import sqlite3

class OfficeTasklist_DB:
    
    def __init__(self):
        self.conn = sqlite3.connect('todo_list.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Todo
                            (  
                                id INTEGER PRIMARY KEY,
                                task varchar(128),
                                date DATE,
                                priority int
                            );
                            ''')

    # Create
    def add_task(self):
        self.clear_console()
        while True:
            task = input("Please enter a Task: ")
            if task:
                while True:
                    date_input = input("Please enter a Date in YYYY-MM-DD format: ")
                    date = self.check_date(date_input)
                    if date != "":
                        date_entered = date
                        while True:
                            print("1. high")
                            print("2. mid")
                            print("3. low")
                            prio_input = input("Please enter 1, 2 or 3: ")
                            priority:int = 0
                            match prio_input:
                                case "1":
                                    priority = 1
                                case "2":
                                    priority = 2
                                case "3":
                                    priority = 3
                                case _:
                                    continue
                            self.cursor.execute(f'''INSERT INTO todo (task, date, priority) VALUES ("{task}","{date_entered}", {priority})''')
                            self.conn.commit()
                            print(f'Task: {task}\t | Date: {date}\t | Priority: {priority} added in Database')
                            input("enter key for main menu...")
                            return
                    

    # Read            
    def show_tasklist(self):
        self.clear_console()
        self.cursor.execute("SELECT * FROM todo")
        results = self.cursor.fetchall()
        if len(results) == 0:
            print("Nothing to see here!")
        else:
            pass
            for todo in results:
                print(f'ID: {todo[0]}\t| Task: {todo[1]}\t | Date: {todo[2]}\t | Priority: {todo[3]}')
        input("enter key for main menu...")
    
    
    # Update
    def update_task(self):
        self.clear_console()
        
        self.cursor.execute("SELECT * FROM todo")
        results = self.cursor.fetchall()
        
        if len(results) == 0:
            print("No entries in DB")
            input("enter key for main menu...")
            return
        
        while True:
            try:
                task_id = int(input("Enter ID or just Enter for exit"))
                self.cursor.execute(f"SELECT * FROM todo WHERE id == {task_id}")
                todo = self.cursor.fetchone()
                print(f'ID: {todo[0]}\t| Task: {todo[1]}\t | Date: {todo[2]}\t | Priority: {todo[3]}')
                
                new_task = todo[1]
                new_date = todo[2]
                new_priority:int = todo[3]
                
                choice = input("Change Task Description? y/n: ")
                if choice == "y":
                    choice = ""
                    new_task = input("Please enter a new Task Description: ")
                    
                choice = input("Change Task Date? y/n: ")
                if choice == "y":
                    choice = ""
                    while True:
                        date_input = input("Please enter a Date in YYYY-MM-DD format: ")
                        date = self.check_date(date_input)
                        if date != "":
                            new_date = date
                            break
                choice = input("Change Task priority? y/n: ")
                if choice == "y":
                    while True:
                            print("1. high")
                            print("2. mid")
                            print("3. low")
                            prio_input = input("Please enter 1, 2 or 3: ")
                            match prio_input:
                                case "1":
                                    new_priority = 1
                                case "2":
                                    new_priority = 2
                                case "3":
                                    new_priority = 3
                                case _:
                                    continue
                            break
                self.cursor.execute(f'''UPDATE todo SET task = "{new_task}", date = "{new_date}", priority = {new_priority} where id == {task_id}''')
                self.conn.commit()
                print("Task Updated...")
                print(f"Old: Task: {todo[1]}\t | Date: {todo[2]}\t | Priority: {todo[3]}")
                print(f"New: Task: {new_task}\t | Date: {new_date}\t | Priority: {new_priority}")
                input("enter key for main menu...")
                return
            except:
                print("Back to Main Menu")
                return
    
    
    # Delete
    def delete_task(self):
        self.clear_console()
        
        self.cursor.execute("SELECT * FROM todo")
        results = self.cursor.fetchall()
        
        if len(results) == 0:
            print("No entries in DB")
            input("enter key for main menu...")
            return
        
        try:
            task_id = int(input("Enter ID or just Enter for exit: "))
            self.cursor.execute(f"SELECT * FROM todo WHERE id == {task_id}")
            todo = self.cursor.fetchone()
            print(f'ID: {todo[0]}\t| Task: {todo[1]}\t | Date: {todo[2]}')
            choice = input("Delete this Task? y/n: ")
            if choice == "y":
                choice = input("Are u sure? y/n: ")
                if choice == "y":
                    self.cursor.execute(f'''delete from todo where id == {task_id}''')
                    self.conn.commit()
                    print("Task deleted...")
                    input("enter key for main menu...")
        except:
            print("Back to Main Menu")
            return
    
    
    def start(self):
        while True:
            self.clear_console()
            print("1. Create Task")
            print("2. Show all Tasks")
            print("3. Update a Task by ID")
            print("4. Delete a Task by ID")
            print("5. Exit")
            
            choice = input("Please enter 1, 2, 3, 4 or 5: ")
            
            match choice:
                case "1":
                    self.add_task()
                case "2":
                    self.show_tasklist()
                case "3":
                    self.update_task()
                case "4":
                    self.delete_task()
                case "5":
                    return
                case _:
                    print("Error, wrong Choice, please enter again!")
                    
                    
    def check_date(self, date_input):
        try:
            return datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except:
            print("Please enter a real Date")
            return ""
        
    def clear_console(self):
        if os.name == 'nt':  
            os.system('cls')
        else:
            os.system('clear')