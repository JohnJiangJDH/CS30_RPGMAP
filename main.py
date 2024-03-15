#####################################################################
# Title: RPG - Dungeons Map
# Class: Computer Science 30
# Assignment: RPG - Map Assignment
# Created By: John Jiang
# Created Date: 12/03/2024
# Version: 1.0
######################################################################
"""
Creating a map for a simple game. As the player moves through the map,
descriptions of the different locations that the user is located in
will be shown. 
"""
######################################################################
# IMPORTS AND GLOBAL VARIABLES ---------------------------------------

loop = True

movementOptions = ["Walk", "Swim", "Fly", "Quit"]

directionOptions = ["Up", "Down", "Left", "Right", "Quit"]

player = {"xLoc": 0, "yLoc": 0}

dungeon_rooms = {
    "Starting Room": {
        "Description": "You have entered some ruins and the "+
        "exploration of a mysterious dungeon awaits you.",
        "Options": ["left", "right"]},
    "Staff Room": {
        "Description": "This room is completely barren, except for the"+
        " presence of a large stone. Stuck inside the stone is none"+
        " other than a staff."},
    "Book Room": {
        "Description": "This room feels ancient. There are images "+
        "carved into all the walls. A floating grimoire sits in the"+
        " centre."},
    "Upgrade Room": {
        "Description": "A crafting bench is situated in the middle "+
        "of the room. The entire room radiates an abundant amount of"+
        " magical energy."},
    "Hallway": {
        "Description": "A long, seemingly endless corridor. The uneven"+
        " rocks beneath your feet make it hard to balance your footing."}
}

dungeon_map = [["Floor One", "Starting Room"],
               ["Floor One", "Staff Room"],
               ["Floor One", "Book Room"],
               ["Floor One", "Upgrade Room"],
               ["Floor Two", "Hallway"]]

######################################################################
# FUNCTIONS ---------------------------------------


def direction():
    try:
        print("Now choose your direction. ")
        count = 0
        for option in directionOptions:
            if count <= len(directionOptions):
                count += 1
                print(f"{count}) {option}")
        directionChoice = int(input("Choose a number: "))
        return directionOptions[directionChoice-1]
    except Exception:
        print("There was an error.")


def mainMenu():
    try:
        count = 0
        for option in movementOptions:
            if count <= len(movementOptions):
                count += 1
                print(f"{count}) {option}")
        movement = int(input("Choose a number: "))
        return movementOptions[movement-1]
    except Exception:
        print("There was an error.")


def main():
    global loop
    try:
        while loop:
            test = mainMenu()
            if test == "Quit":
                return print("Quitting...")
            elif test is not None:
                print(test)
                print("\n")
                loop = False
                direction()
            else:
                print("Try again.")
    except Exception:
        print("There was an error.")
        

######################################################################
# MAIN ---------------------------------------

main()