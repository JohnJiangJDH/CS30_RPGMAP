######################################################################
# Module: Inventory
######################################################################
"""
This module contains anything related to the inventory functions.
"""
######################################################################

# Database of collectible items and definitions
items = {
    "Staff": {
        "Description": "A sturdy staff radiating an immense aura."},
    "Grimoire": {
        "Description": "A grimoire imbued with magic energy. Within it"+
        " contains a new, undiscovered spell."}
}

######################################################################
# FUNCTIONS ---------------------------------------


def inventoryMenu(inventory):
    """
    This function creates the menu that displays the user's inventory
    """
    try:
        # Loop through list of inventory items
        for item in inventory:
            # Print the current amount of each item
            print(f"You currently have {inventory[item]} {item}s")
    except Exception:
        print("There was an error.")


def itemMap(dungeonMap, dungeonRooms):
    """
    This function creates a map of the status of items in each room
    of the dungeon.
    """
    try:
        listOne = []
        listTwo = []
        # For the length of the dungeon's vertical(y) floors:
        for y in range(len(dungeonMap)):
            # Clear first list each time
            listOne = []
            # For each room horizontally(x):
            for x in dungeonMap[y]:
                # Add the item status(T/F) of that room to first list
                listOne.append(dungeonRooms[x]["ItemStatus"])
            # Append first list, which is the first vertical "floor"
            # of the dungeon, to a new second list
            listTwo.append(listOne)
        return listTwo
    except Exception:
        print("There was an error.")


def takeItem(currentRoom, currentItemStatus):
    """
    This function takes an item from a room depending on the specifics
    of the room (availability of item) as well as if the item had
    already previously been collected.
    """
    try:
        # If the current room is a room with an item aka Staff or Book,
        # And If the item is still there:
        if currentRoom == "Staff Room" and currentItemStatus:
            # Print descriptions of collecting the item
            print("You release the staff from the stone and examine it:")
            # Print item description
            print(items["Staff"]["Description"])
            print("You place the staff into your inventory.")
            print("\n")
            return "Staff"
        elif currentRoom == "Book Room" and currentItemStatus:
            print("You embrace the book and examine it:")
            print(items["Grimoire"]["Description"])
            print("You place the book into your inventory.")
            print("\n")
            return "Book"
        else:
            # Otherwise, the room either has no item in the first place,
            # or had an item but was previously already taken
            print("There is nothing noteworthy to find here.")
            print("\n")
    except Exception:
        print("There was an error.")