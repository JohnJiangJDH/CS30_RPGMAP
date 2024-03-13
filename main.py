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

#player = {xLoc: 0, }

dungeon_rooms = {"Starting Room": {"Description": "You have entered\
some ruins and the exploration of a mysterious dungeon awaits you. ",
                                 "Options": ["left", "right"]}}


# dungeon_map = [[startFloor, startRoom],
#                [startFloor, staffRoom],
#                [startFloor, bookRoom],
#                [startFloor, upgradeRoom]]



######################################################################
# FUNCTIONS ---------------------------------------


def mainMenu():
    try:
        count = 0
        for option in movementOptions:
            if count <= len(movementOptions):
                count += 1
                print(f"{count}) {option}")
                
        movement = int(input("Choose a movement option: "))
        return movementOptions[movement-1]
        
    except Exception:
        print("There was an error.")


def main():
    global loop
    try:
        while loop:
            test = mainMenu()
            if not test is None or test != "Quit":
                print(test)
                loop = False
            else:
                print("Try again.")
    
    except Exception:
        print("There was an error.")
        

######################################################################
# MAIN ---------------------------------------

main()