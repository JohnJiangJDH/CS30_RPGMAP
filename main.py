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

# List of movement options for main menu
movementOptions = ["Walk", "Swim", "Fly", "Quit"]
# List of direction options for sub menu
directionOptions = ["Up", "Down", "Left", "Right", "Quit"]
# Player coordinates to save current location. Begins at starting room (0,0)
player = {"xLoc": 0, "yLoc": 0}
# Database for the name and description of each individual room on map
dungeon_rooms = {
    "Starting Room": {
        "Description": "You have entered some ruins and the "+
        "exploration of a mysterious dungeon awaits you."},
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
        " rocks beneath your feet make it hard to balance your footing."},
    "Eternal Slumber": {
        "Description": "A room with a relaxing aura, dimly lit by torches."+
        " The Queen, previous ruler of this area, now rests inside the"+
        " coffin layered with flowers."},
    "Feasting Room": {
        "Description": "Numerous tables stand organized before you in"+
        " long rows. There is an assortment of deliciously looking"+
        " delicacies awaiting."}
}
# Layout of map with rooms in a 4x3 multi-dimensional list
dungeon_map = [
    ["Starting Room", "Staff Room", "Upgrade Room", "Book Room"],
    ["Eternal Slumber", "Book Room", "Hallway", "Staff Room"],
    ["Staff Room", "Feasting Room", "Book Room", "Hallway"],
]

######################################################################
# FUNCTIONS ---------------------------------------


def direction():
    """
    This function creates the sub menu for the user to choose the 
    direction they want to move in
    """
    try:
        print("Now choose your direction. ")
        count = 0
        # Loop through list of direction options aka up down left right
        for option in directionOptions:
            # Give each listed option an identifier ie 1), 2), 3), etc.
            if count <= len(directionOptions):
                count += 1
                print(f"{count}) {option}") # Print options
        # User input to choose direction, only allows index number
        directionChoice = int(input("CHOOSE A NUMBER: "))
        # Return the direction option chosen from the list
        return directionOptions[directionChoice-1]
    except Exception:
        print("There was an error. Read instructions carefully and check your input.")


def mainMenu():
    """
    This function creates the main menu for the user to choose their
    movement option
    """
    try:
        count = 0
        # Loop through list of movement options aka walk, swim, fly
        for option in movementOptions:
            # Give each listed option an identifier ie 1), 2), 3), etc.
            if count <= len(movementOptions):
                count += 1
                print(f"{count}) {option}") # Print options
        # User input to choose movement, only allows index number
        movement = int(input("CHOOSE A NUMBER: "))
        # Return the movement option chosen from the list
        return movementOptions[movement-1]
    except Exception:
        print("There was an error. Read instructions carefully and check your input.")


def movePlayer(direct):
    """
    This function moves the player by adjusting their
    location/coordinates accordingly to what was chosen
    """
    try:
        # Depending on the direction chosen, player coordinates
        # are updated from the previous coordinates
        if direct == "Up":
            player["yLoc"] -= 1
        elif direct == "Down":
            player["yLoc"] += 1
        elif direct == "Left":
            player["xLoc"] -= 1
        elif direct == "Right":
            player["xLoc"] += 1
    except Exception:
        print("There was an error.")


def main():
    """Main function responsible for calling other functions"""
    loop = True
    try:
        # Print the initial room that the player starts in
        print(dungeon_rooms["Starting Room"]["Description"])
        # While for continuous main menu
        while loop:
            # Call and check validity of player's choice of movement
            firstMenu = mainMenu()
            if firstMenu == "Quit":
                return print("Quitting...") # Return if quit is chosen
            elif firstMenu is not None:
                # Otherwise, the movement choice chosen is valid
                print(f"You have chosen to {firstMenu}")
                print("\n")
                # No need to loop the main menu anymore
                loop = False
                # Second while loop for continuous sub menu
                secondLoop = True
                while secondLoop: 
                    # Call and check validity of player's choice of direction
                    choice = direction()
                    if choice == "Quit":
                        return print("Quitting...") # Return if quit is chosen
                    elif choice is not None:
                        # Otherwise, the direction choice chosen is valid
                        print("\n")
                        # Call function to update the player's coordinates
                        movePlayer(choice)
                        print("\n")
                        
                        # After player's coordinates are adjusted,
                        # Check if the direction chosen makes the player
                        # go out of the map's boundaries

                        # If so, then do the opposite operation of
                        # whichever direction option was chosen to reset
                        # Player's coordinates to the most recently valid 
                        if player["yLoc"] < 0:
                            player["yLoc"] += 1
                            print("You have reached the border and cannot go further.")
                        elif player["yLoc"] > 2:
                            player["yLoc"] -= 1
                            print("You have reached the border and cannot go further.")
                        elif player["xLoc"] < 0:
                            player["xLoc"] += 1
                            print("You have reached the border and cannot go further.")
                        elif player["xLoc"] > 3:
                            player["xLoc"] -= 1
                            print("You have reached the border and cannot go further.")
                        else:
                            # If the player is inside the map
                            # Enter Player coordinates into map to find
                            # the room that the Player is currently located in
                            playerLocation = dungeon_map[player["yLoc"]][player["xLoc"]]
                            # Print that current room's description
                            print(dungeon_rooms[playerLocation]["Description"])
                            # While loop makes this sub menu continuous
                            # So Player continues forward
                            print("You continue forward.")
                            print("\n")
                    else:
                        print("Try again.")
                        print("\n")
            else:
                print("Try again.")
                print("\n")
    except Exception:
        print("There was an error.")
        

######################################################################
# MAIN ---------------------------------------


main()