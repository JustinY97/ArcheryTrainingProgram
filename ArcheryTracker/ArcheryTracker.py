### Training Tracker for Archery Events ###
from datetime import date
import json, os
from time import sleep

targetList = ["Strutting Turkey", "Javelina", "Coyote", "Wild Boar", "Russian Boar", "Howling Wolf", "Auodad", "Brown Bear", "Lynx", "Warthog", "African Leopard", "African Blesbok", "Tapir", "Wolverin", "Chamois", "Black Panther", "Large Alert Deer", "Medium Deer", "Hill Country Whitetail", "Extea Large Deer"]


### CLEARS TERMINAL WINDOW ###
def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

def menu():
    print("Select Choice")
    print("1. Add Event")
    print("2. View Event")
    print("3. Edit Event")
    print("4. Exit")
    user = int(input("Select choice...\n"))
    clear()
    return user

def editEvent(lst):
    print("Inside EditEvent Function")

def add3DEvent(lst):
    title = input("Enter Title of Event: ")
    newEvent = {"Title" : title, "Date" : str(date.today()), "Targets" : {}}
    lst.append(newEvent)
    events.update({"3D Events" : lst})

def add3DTarget(lst):
    print(lst)

def addIndoorEvent(lst):
    title = input("Enter Title of Event: ")
    newEvent = {"Title" : title, "Date" : str(date.today()), "Targets" : {}}
    lst.append(newEvent)
    events.update({"Indoor Events" : lst})
    
def addOutdoorEvent(lst):
    title = input("Enter Title of Event: ")
    newEvent = {"Title" : title, "Date" : str(date.today()), "Targets" : {}}
    lst.append(newEvent)
    events.update({"Outdoor Events" : lst})

def editEvent(event):
    print("Inside Function")
    sleep(1)

def getEvent(eventTitle):
    for eventType in events.values():
        print(eventType)

        


    ### MAIN ###
events = json.load(open('ArcheryTracker/Data/events.json', 'r+'))

while True:
    print("Select Choice")
    print("1. Add Event")
    print("2. View Event")
    print("3. Edit Event")
    print("4. Exit")
    print("5. Test")
    user = int(input())
    clear()

    if user == 1:
        print("Type of Event")
        print("1. 3D Event")
        print("2. Indoor Event")
        print("3. Outdoor Event")
        event = int(input("Enter Choice...\n"))
        clear()

        if event == 1:
            add3DEvent(events.get("3D Events"))
        elif event == 2:
            addIndoorEvent(events.get("Indoor Events"))
        elif event == 3:
            addOutdoorEvent(events.get("Outdoor Events"))

    ### VIEW A SPECIFIC EVENT ###
    elif user == 2:
        temp = printEvents()
            
        ### PICK AN EVENT TITLE AND FIND THAT EVENT INFO ###

        ### ASK TO SAVE INFO AND SAVE ###


    ### EDIT AN EVENT ###
    elif user == 3:

        ### PRINT LIST OF EVENTS WITH NUMBERS AND RETURN THE EVENT INFO ###
        eventList = printEvents()
        
        eventID = input("Event Title/Number\n")
        clear()
        try:
            eventID = int(eventID)
            eventID = eventList[eventID - 1]
            event = getEvent(eventID)
        except(Exception):
            event = getEvent(eventID)




    elif user == 4:
        print("Exiting and Saving...")
        sleep(1.5)
        clear()
        break

        

json.dump(events, open('ArcheryTracker/Data/events.json', 'r+'), indent=2)

