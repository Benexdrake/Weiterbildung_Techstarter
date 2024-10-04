import datetime

class OfficeTasklist:
    
    def __init__(self):
        self.__todoList = []
        
    # Feature 1 add task
    
    ## 1. Nutze die `input`-Funktion, um den User nach einer Büroaufgabe zu fragen, z.B.: „Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll“. 
    ## 2. Speichere die Eingabe in der Variablen `task`. 
    ## 3. Füge die Aufgabe zur Liste hinzu. 
    ## 4. Gib eine Meldung aus, dass die Aufgabe zur Liste hinzugefügt wurde. 

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
                        
    # Feature 2 show tasklist
    
    ## 1. Prüfe, ob die Liste leer ist. Wenn ja, gib den Text „Deine Aufgabenliste ist leer“ aus. 
    ## 2. Wenn die Liste nicht leer ist, drucke alle Aufgaben mit einer `for`-Schleife. 
    ## 3. Gib auch das Fälligkeitsdatum (falls vorhanden) mit aus. 

    def show_tasklist(self):
        if not self.__todoList:
            print("Nothing to see here!")
        else:
            for index,todo in enumerate(self.__todoList):
                print(f'ID: {index+1}\t| Task: {todo["task"]}\t | Date: {todo["date"]}')

    # Feature 3 Main Menu
    
    ## 1. Erstelle eine `while`-Schleife, die den User fragt, ob er eine Aufgabe hinzufügen, 
    # die Liste anzeigen oder das Programm beenden möchte. 
    ## 2. Nutze eine `if/elif`-Bedingung, um die Eingabe des Users zu verarbeiten. 