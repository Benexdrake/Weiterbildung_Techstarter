shoppingList = []

# 1. Erstelle einen branch namens feature/create-add-function
## Erstelle eine Methode namens add_item
### input "Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll"
### Speichern der Antwort in Variable item
### einfügen von item in globaler Liste
### print Artikel der Liste hinzugefügt
### Erstelle einen Pull Request auf Github und pull lokal

def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    shoppingList.append(item)
    print(f"Wurde der Liste hinzugefügt: {item}")

# 2. Erstelle einen branch namens feature/add-show-shoppinglist-function
## Erweitere das Script mit der Methode show_shoppinglist
### Überprüfe ob shoppinglist länge 0 ist
#### True: print shoppingliste leer
#### False: Ausgabe der Shoppingliste per print
## Erstelle einen Pull Request auf Github und pull lokal

def show_shopping_list():
    if len(shoppingList) == 0:
        print("Deine Einkaufsliste ist leer")
    else:
        for item in shoppingList:
            print(f"{item}")

# 3. Erstelle einen branch namens feature/add-main-function
## Erstelle eine main Methode
### Füge eine While Schleife mit True hinzu
#### print ----- Einkaufsliste -----
#### print 3 Auswahlmöglichkeiten
#### 1. Artikel zur Einkaufsliste hinzufügen
#### 2. Einkaufsliste anzeigen
#### 3. Programm beenden
### Frage per Input nach einer Zahl, 1,2,3, gibt der User was falsches an, soll eine fehlermeldung angezeigt werden.
### Überprüfe per if elif else die Eingabe
#### 1 aufruf add_item Methode
#### 2 aufruf show_shoppinglist Methode
#### 3 break oder return zum abbrechen des progamms
#### else print fehlermeldung
## Erstelle einen Pull Request auf Github und pull lokal danach

def main():
    while True:
        print("----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")

        select = input("Wähle bitte zwischen 1-3 aus:")
        match select:
            case "1":
                add_item()
            case "2": 
                show_shopping_list()
            case "3":
                print("Programm wird beendet")
                return
            case _:
                print("Was war an 1-3 unverständlich?")
        


# 4. Erstelle einen branch namens feature/add-automatic-run-function
## Füge eine if abfrage für __name == "__main__" hinzu und rufe dort main() auf
## Erstelle einen Pull Request auf Github und einen pull lokal

from einkaufsliste import Einkaufsliste

if __name__ == "__main__":
    #main()
    einkauf = Einkaufsliste()
    einkauf.start()