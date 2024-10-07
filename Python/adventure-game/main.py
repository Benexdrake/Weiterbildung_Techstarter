import random
from game_utils import enter_room,solve_riddle,start_game,end_game,clear_console



def main():
    rooms = start_game()
    # random auswahl von Room
    enter_room(rooms[0])
    rooms.remove(rooms[0])
    
    while len(rooms) > 1:
        # Ablauf
        # random index
        clear_console()
        index = random.randint(0, len(rooms)-2)
        
        # auswahl rooms[index]
        room = rooms[index]
        # enter_room
        enter_room(room)
        rooms.remove(rooms[index])
        # Ausgabe des Raum namens mit einer kleinen Beschreibung, was man so sieht.
        # Raum kann ein Rätsel oder eine Kiste haben mit einem Item drin.
        
        # Raum kann bis zu 4 Wege beinhalten.
        # Ausgabe der Räume und abfrage zwischen 1-len auswahl
        
        # fängt von oben wieder an.
    print(len(rooms))
    enter_room(rooms[0])
    end_game()
    
    
main()