# def aufgabe1(_first_name:str, _last_name:str, _has_license:bool):
#     first_name:str = _first_name
#     last_name:str = _last_name
#     has_license:bool = _has_license

#     result = {"FirstName":first_name,"LastName":last_name,"License":has_license}
#     print(f"Aufgabe1: {result}")
#     print(f"Vorname: {first_name}\nNachname: {last_name}\nLizenz: {has_license}")


# def aufgabe2(a:int, b:int):
#     sum:int = a + b
#     dif:int = a - b
#     produkt = a * b
#     quotient = a // b
#     rest = a % b
#     potenz = a ** b
#     result = {"Summe":sum, "Differenz": dif, "Produkt": produkt, "Quotient": quotient, "Rest": rest, "Potenz": potenz}
#     print(f"Aufgabe2: {result}")
    

# def celsius_to_fahrenheit(c:int|float):
#     result = 9/5 * c + 32
#     print(f"Fahrenheit: {result}")


# def price_to_tax(price:int|float):
#     result = price * 1.19
#     print(f"Price with Tax: {result}")

# list_test = [1, "test", aufgabe1("","",True)]
# array_test = [1,2,3,4,5,6]

# test = []
# test.append(aufgabe1("BeneX","Drake",False))
# test.append(aufgabe2(10,3))
# test.append(celsius_to_fahrenheit(25))
# test.append(celsius_to_fahrenheit(10))
# test.append(price_to_tax(10))

# for t in test:
#     t

# aufgabe1("BeneX","Drake",False)
# aufgabe2(10,3)
# celsius_to_fahrenheit(25)
# celsius_to_fahrenheit(10)
# price_to_tax(10)

# x = range(1,5)


# for y in x:
#     print(y)
    
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('studenten.db')

# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

# Tabelle erstellen (falls nicht existiert)
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
''')

# Daten in die Tabelle einfügen
def student_hinzufuegen(name, age, course):
    cursor.execute('''
    INSERT INTO students (name, age, course) 
    VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f'Student {name} hinzugefügt.')

# Daten abrufen
def studenten_anzeigen():
    cursor.execute('SELECT * FROM students')
    studenten = cursor.fetchall()
    print("Alle Studenten:")
    for student in studenten:
        print(student)

# Beispielaufrufe
student_hinzufuegen("Max Mustermann", 21, "Informatik")
student_hinzufuegen("Anna Schmidt", 22, "Mathematik")
student_hinzufuegen("Lisa Müller", 20, "Physik")

studenten_anzeigen()

# Verbindung schließen
conn.close()