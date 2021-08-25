import json
import os
from time import sleep
import datetime

def exit(filePath, data):
    saveFlag = input("Save changes? (Y/N): ")
    if saveFlag.upper() == "Y":
        print("Exiting and Saving...")
        sleep(1)
        clear()
        json.dump(data, open(filePath, 'r+'), indent=2)
        os.system("exit")

    else:
        print("Exiting without saving...")
        sleep(1)
        clear()
        os.system("exit")

def clear():
    os.system("clear")

def printEvents(data):
    for events in data.values():
        for val in events:
            print(val.get("Title"))

def printTargets(targetList):
    for target in targetList:
        print("%d. Score: %d\t Yardage: %.1f" %(target.get("Target Num"), target.get("Score"), target.get("Yardage")))

def Menu():
    print("1. View an Event")
    print("2. Edit an Event")
    print("3. Add a new Event")
    print("4. Quit")
    userInput = int(input())
    clear()
    return userInput

def addEvent(events):
    types = []
    for val in events.keys():
        print("%d. %s" %(list(events.keys()).index(val) + 1, val))
        types.append(val)

    eventType = input("Event Type: ")
    clear()
    try:
        eventType = int(eventType)        
        eventType = types[eventType - 1]
    except:
        eventType = str(eventType)
    
    for val in events.items():
        if eventType == val[0]:
            eventTitle = input(str("Name of new %s: " % (eventType)))
            newEvent = {"Title": eventTitle, "Date" : str(datetime.date), "Targets" : []}
            val[1].append(newEvent)

    editEvent(newEvent)

## function to add a target ##
def addTarget(targetList):
    ## Target Format {"Target Num" : int, "Score" : int, "Yardage" : float}
    score = int(input("Score: "))
    yardage = float(input("Yardage: "))
    clear()
    targetList.append({"Target Num" : int(len(targetList) + 1), "Score" : score, "Yardage": yardage})
    

## Pass in the event Dictionary ##
def editEvent(event):
    print("Edit Menu")
    print("1. Change Title")
    print("2. Add Target")
    print("3. Edit Target")
    print("9. Delete Event")
    choice = int(input())
    clear()
    if choice == 1:
        event["Title"] = input("New Title: ")
    elif choice == 2:
        addTarget(event.get("Targets"))
    elif choice == 3:
        printTargets(event.get("Targets"))
        targetNum = int(input("Enter target number to edit: "))
        editTarget(list(event.get("Targets"))[targetNum - 1])

def editTarget(target):
    print("Inside edit Target function")
    print(target)
    ## Edit Target Menu ## (Be able to edit Score and Yardage)


def viewEvent(event):
    print("Title: %s\nDate: %s\nTargets\n" %(event.get("Title"), event.get("Date")))
    for val in event.get("Targets"):
        print(val)

def getEvent(data):
    printEvents(data)
    eventTitle = input("Enter Event Title\n")
    clear()
    for events in data.values():
        for val in events:
            if val.get("Title") == eventTitle:
                return val


## MAIN ##
data = json.load(open('/Users/justinyork/Programs/ArcheryTrainingProgram/ArcheryTracker/Data/events.json', 'r+'))
## Return to main menu ##
while True:
    menuChoice = Menu()
    ## VIEW AN EVENT ##
    if menuChoice == 1:
        viewEvent(getEvent(data))

    ## EDIT AN EVENT ##
    elif menuChoice == 2:
        editEvent(getEvent(data))

    ## ADD EN EVENT ##    
    elif menuChoice == 3:
        addEvent()
    
    ## QUIT ##
    elif menuChoice == 4:
        exit('/Users/justinyork/Programs/ArcheryTrainingProgram/ArcheryTracker/Data/events.json', data)
        break

    ## Default ##
    else:
        print("Invalid Choice")
    
    returnToMenu = input("Return to Menu? (Y/N): ").upper()
    if returnToMenu == "N":
        exit('/Users/justinyork/Programs/ArcheryTrainingProgram/ArcheryTracker/Data/events.json', data)
        break
