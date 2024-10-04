import datetime

class OfficeTasklist:
    
    def __init__(self):
        self.__todoList = []

    def add_task(self):
        while True:
            task = input("Please enter a Task: ")
            if task:
                while True:
                    date_input = input("Please enter a Date in YYYY-MM-DD format: ")
                    try:
                        date_entered = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                        self.__todoList.append({"task":task, "date": date_entered})
                        return
                    except:
                        print("Please enter a real Date")
                        
    def show_tasklist(self):
        if not self.__todoList:
            print("Nothing to see here!")
        else:
            for index,todo in enumerate(self.__todoList):
                print(f'ID: {index+1}\t| Task: {todo["task"]}\t | Date: {todo["date"]}')
    
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
                return
            else:
                print("Error, wrong Choice, please enter again!")