######################################################################
# Module: Inventory
######################################################################
"""
This module contains anything related to the inventory functions.
"""
######################################################################

# Database of collectible items and attributes
items = {
    "Staff": {
        "Description": "A sturdy staff radiating an immense aura."},
    "Grimoire": {
        "Description": "A grimoire imbued with magic energy. Within it"+
        " contains a new, undiscovered spell."}
}


def inventoryMenu(inventory):
    """
    This function creates the menu that displays the users inventory
    """
    try:
        # Loop through list of inventory items
        for item in inventory:
            # Print the current amount of each item
            print(f"You currently have {inventory[item]} {item}s")
    except Exception:
        print("There was an error.")


def takeItem(currentRoom, currentItemStatus):
    if currentRoom == "Staff Room":
        if currentItemStatus:
            print("You release the staff from the stone and examine it:")
            print(items["Staff"]["Description"])
            print("You place the staff into your inventory.")
            print("\n")
            return "Staff"
        else:
            print("There is nothing noteworthy to find here.")
            print("\n")
    elif currentRoom == "Book Room":
        if currentItemStatus:
            print("You embrace the book and examine it:")
            print(items["Grimoire"]["Description"])
            print("You place the book into your inventory.")
            print("\n")
            return "Book"
        else:
            print("There is nothing noteworthy to find here.")
            print("\n")
    else:
        print("There is nothing noteworthy to find here.")
        print("\n")