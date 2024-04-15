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


def takeItem(currentRoom, currentItemStatus):
    if currentRoom == "Staff Room":
        if currentItemStatus:
            print("You release the staff from the stone and examine it.")
            print("\n")
            print(items["Staff"]["Description"])
            print("\n")
            print("You place the staff into your inventory.")
    elif currentRoom == "Book Room":
        print("You embrace the book and examine it.")
        print("\n")
        print(items["Grimoire"]["Description"])
        print("\n")
        print("You place the book into your inventory.")
    else:
        print("There is nothing noteworthy to find here.")