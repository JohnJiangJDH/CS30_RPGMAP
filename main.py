######################################################################
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

# Import Player module
import player
# Import Map module
import map
# Import Inventory module
import inventory
# Import Menu module
import menu

# Player class
playerClass = player.Player()
#Map of item statuses in each room
itemStatusMap = map.ItemMap().itemMap()

######################################################################
# FUNCTIONS ---------------------------------------


def movePlayer(direct):
    """
    This function moves the player by adjusting their
    location/coordinates accordingly to what was chosen
    """
    try:
        # Depending on the direction chosen, player coordinates
        # are updated from the previous coordinates
        if direct == "Up":
            playerClass.player["yLoc"] -= 1
        elif direct == "Down":
            playerClass.player["yLoc"] += 1
        elif direct == "Left":
            playerClass.player["xLoc"] -= 1
        elif direct == "Right":
            playerClass.player["xLoc"] += 1
    except Exception:
        print("There was an error.")


def resetCoordinates():
    """This function checks if the player goes out of boundaries"""
    # After player's coordinates are adjusted
    # Check if the direction chosen makes the player
    # go out of the map's boundaries
    # If so, then do the opposite operation of
    # whichever direction option was chosen to reset
    # Player's coordinates to the most recently valid 
    if playerClass.player["yLoc"] < 0:
        playerClass.player["yLoc"] += 1
        print("You have reached the border and cannot go further.")
        return True
    elif playerClass.player["yLoc"] > 2:
        playerClass.player["yLoc"] -= 1
        print("You have reached the border and cannot go further.")
        return True
    elif playerClass.player["xLoc"] < 0:
        playerClass.player["xLoc"] += 1
        print("You have reached the border and cannot go further.")
        return True
    elif playerClass.player["xLoc"] > 3:
        playerClass.player["xLoc"] -= 1
        print("You have reached the border and cannot go further.")
        return True
    else:
        return False
    

def subMenu():
    """This function processes all of the player's choices in submenu"""
    # Check player's option
    choice = menu.menuSub.createMenu()
    if choice == "Quit":
        return print("Quitting...") # Return if quit is chosen
    elif choice == "Back":
        # If choice is to go back to main menu, submenu loop off
        print("\n")
        print("Choose an option.")
        return True
    elif choice == "Search The Area":
        print("\n")
        # If Search The Area is chosen:
        # Get current player location
        playerLocation = \
        map.Map().dungeon_map[playerClass.player["yLoc"]][playerClass.player["xLoc"]]
        # Get current status of item in room
        itemStatus = \
        itemStatusMap[playerClass.player["yLoc"]][playerClass.player["xLoc"]]
        # Take item, depending on the current room
        # And item status
        item = inventory.takeItem(playerLocation, itemLocation)
        # Set current room's item status to False
        # Because cannot collect a second time
        item_status_map[player["yLoc"]][player["xLoc"]] = False

    elif choice is not None:
        # Otherwise, the direction choice chosen is valid
        # Call function to update the player's coordinates
        movePlayer(choice)
        print("\n")



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
    
def main():
    """Main function responsible for calling other functions"""
    loop = True
    try:
        # Print the initial room that the player starts in
        print(dungeon_rooms["Starting Room"]["Description"])
        # Player begins with map when entering dungeon
        map.writeFile()
        # While for continuous main menu
        while loop:
            # Call and check validity of player's choice of movement
            firstMenu = mainMenu()
            if firstMenu == "Quit":
                return print("Quitting...") # Return if quit is chosen
            elif firstMenu == "View Map":
                print("\n")
                # If view map is chosen, print the map to console
                # Since we already begin with the map in
                # External file
                map.readFile()
            elif firstMenu == "Check Inventory":
                print("\n")
                # If Check Inventory is chosen:
                # Print a menu with the names and amounts of items
                # That are currently in the inventory. Initially 0.
                inventory.inventoryMenu(inventoryItems)
                print("\n")
            elif firstMenu is not None:
                # Otherwise, the movement choice chosen is valid
                print(f"You have chosen to {firstMenu}")
                print("\n")
                # No need to loop the main menu anymore
                loop = False
                # Second while loop for continuous sub menu
                secondLoop = True
                while secondLoop: 
                    
            else:
                print("Try again.")
                print("\n")
    except Exception:
        print("There was an error.")
        

######################################################################
# MAIN ---------------------------------------


main()