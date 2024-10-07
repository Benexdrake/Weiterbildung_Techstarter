import json
import os

rooms = []

def load_rooms():
    with open('rooms.json', 'r') as file:
        return json.load(file)

def greeting():
    print("Welcome Player")

def enter_room(room):
    print(room["name"])
    print(room["description"])
    
    if room["riddle"]["question"] != "":
        solve_riddle(room["riddle"])
    
    for index,choice in enumerate(room["choices"]):
        print(f"{index +1}. {choice}")
    
    question = "Please choose between 1 and " + str(len(room["choices"]))
    
    while True:
        try:
            choice = int(input(question))
            
            choices = list(range(1,len(room["choices"])+1))
            if choice in choices:
                break
            else:
                print(choice)
                print(choices)
        except:
            print("wrong choice")
        
    
def solve_riddle(riddle):
    while True:
        answer = input(riddle["question"])
        if answer.lower() in str(riddle["answer"]):
            print("Yes, the right Answer is: " + str(riddle["answer"]))
            break

def start_game():
    return load_rooms()

def end_game():
    print("Great, u finished the Game!")
    

def clear_console():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')