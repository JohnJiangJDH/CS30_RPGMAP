######################################################################
# Module: Inventory
######################################################################
"""
This module contains anything related to the inventory functions.
"""
######################################################################

class Inventory:
    def __init__(self):
        # Database of collectible items and definitions
        self.items = {
            "Staff": {
                "Description": "A sturdy staff radiating an immense aura."},
            "Grimoire": {
                "Description": "A grimoire imbued with magic energy. Within it"+
                " contains a new, undiscovered spell."}
        }
        #Items in Inventory 
        self.inventoryItems = {
            "Staff": 0,
            "Book": 0
        }

    def inventoryMenu(self):
        """
        This function creates the menu that displays the user's inventory
        """
        try:
            # Loop through list of inventory items
            for item in self.inventoryItems:
                # Print the current amount of each item
                print(f"You currently have {self.inventoryItems[item]} {item}s")
        except Exception:
            print("There was an error.")

    def takeItem(self, currentRoom, currentItemStatus):
        """
        This function takes an item from a room depending on the specifics
        of the room (availability of item) as well as if the item had
        already previously been collected.
        """
        self.currentRoom = currentRoom
        self.currentItemStatus = currentItemStatus
        try:
            # If the current room is a room with an item aka Staff or Book,
            # And If the item is still there:
            if self.currentRoom == "Staff Room" and self.currentItemStatus:
                # Print descriptions of collecting the item
                print("You release the staff from the stone and examine it:")
                # Print item description
                print(self.items["Staff"]["Description"])
                print("You place the staff into your inventory.")
                print("\n")
                return "Staff"
            elif self.currentRoom == "Book Room" and self.currentItemStatus:
                print("You embrace the book and examine it:")
                print(self.items["Grimoire"]["Description"])
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

    def updateItem(self, itemGotten):
        """This function updates the user's inventory"""
        self.itemGotten = itemGotten
        # If item was successfully collected:
        # Update inventory items and amounts as needed
        if self.itemGotten == "Staff":
            self.inventoryItems["Staff"] += 1
        elif self.itemGotten == "Book":
            self.inventoryItems["Book"] += 1        

######################################################################
# FUNCTIONS ---------------------------------------
