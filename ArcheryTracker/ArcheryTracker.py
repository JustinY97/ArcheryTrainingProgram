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

def getEvent(eventTitle):
    for eventType in events.values():
        for val in eventType:
            return val

### MAIN ###

events = json.load(open('ArcheryTracker/Data/events.json', 'r+'))

while True:
    user = menu()

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
        eventList = []
        for val in events.values():
            for evnt in val:
                eventList.append(evnt.get("Title"))
                
        eventList.sort()
        for i in range(eventList.__len__()):
            print(str(i + 1) + ". " + eventList[i])
        
        ### PICK AN EVENT TITLE AND FIND THAT EVENT INFO ###
        eventID = input("Enter Event Title or ID\n")
        try:
            eventID = int(eventID)
            eventID = eventList[int(eventID)- 1]
            clear()
        except:
            clear()

        evnt = getEvent(eventID)
        print(evnt)

    ### QUIT ###
    elif user == 4:
        try:
            save = int(input("1. Save\n2. Exit without saving\n"))
            sleep(2)
            clear()
    
            if save == 1:
                json.dump(events, open('ArcheryTracker/Data/events.json', 'r+'), indent=2)
            elif save == 2:
                save = input("Are you sure you want to quit without saving! (Y/N)\n")
                save = str.upper(save)
                if save == "Y":
                    print("Exiting without saving...")  
                elif save == "N":
                    print("Saving...")
                    json.dump(events, open("ArcheryTracker/Data/events.json", "r+"), indent=2)
        except(Exception):
            print("Error in input")

        break
