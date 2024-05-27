######################################################################
# Module: Map
######################################################################
"""
This module contains anything related to the map/external files
functions.
"""
######################################################################

# Import tabulate for map table
from tabulate import tabulate

class Map:
    def __init__(self):  
        # The file containing the map of dungeon
        self.mapFile = "map.txt"
        # Layout of map with rooms in a 4x3 multi-dimensional list
        self.dungeon_map = [
            ["Starting Room", "Staff Room", "Upgrade Room", "Book Room"],
            ["Eternal Slumber", "Book Room", "Hallway", "Staff Room"],
            ["Staff Room", "Feasting Room", "Book Room", "Hallway"],
        ]
        # Database for the name and description of each individual room on map
        self.dungeon_rooms = {
            "Starting Room": {
                "Description": "You have entered some ruins and the "+
                "exploration of a mysterious dungeon awaits you.",
                "ItemStatus": False},
            "Staff Room": {
                "Description": "This room is completely barren, except for the"+
                " presence of a large stone. Stuck inside the stone is none"+
                " other than a staff.",
                "ItemStatus": True},
            "Book Room": {
                "Description": "This room feels ancient. There are images "+
                "carved into all the walls. A floating grimoire sits in the"+
                " centre.",
                "ItemStatus": True},
            "Upgrade Room": {
                "Description": "A crafting bench is situated in the middle "+
                "of the room. The entire room radiates an abundant amount of"+
                " magical energy.",
                "ItemStatus": False},
            "Hallway": {
                "Description": "A long, seemingly endless corridor. The uneven"+
                " rocks beneath your feet make it hard to balance your footing.",
                "ItemStatus": False},
            "Eternal Slumber": {
                "Description": "A room with a relaxing aura, dimly lit by torches."+
                " The Queen, previous ruler of this area, now rests inside the"+
                " coffin layered with flowers.",
                "ItemStatus": False},
            "Feasting Room": {
                "Description": "Numerous tables stand organized before you in"+
                " long rows. There is an assortment of deliciously looking"+
                " delicacies awaiting.",
                "ItemStatus": False}
        }

    def writeFile(self):
        """This function writes the map to an external file."""
        global mapFile
        try:
            with open(self.mapFile, 'w') as file:
                file.write(tabulate(self.dungeon_map, tablefmt = "grid"))
        except:
            print("An error occurred when writing the file.")
        else:
            print("\n")
            print("You have a map of the dungeon with you.")
        finally:
            print("Use it to your advantage.")
            print("\n")

    def readFile(self):
        """
        This function reads an external file to print the map 
        to the console.
        """
        try:
            with open(self.mapFile, 'r') as file:
                print(file.read())
        except:
            print("An error occurred when reading the file.")
        else:
            print("What a useful map.")
        finally:
            print("You continue forward.")
            print("\n")

######################################################################
# FUNCTIONS ---------------------------------------





