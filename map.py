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
# The file containing the map of dungeon
mapFile = "map.txt"
# Layout of map with rooms in a 4x3 multi-dimensional list
dungeon_map = [
    ["Starting Room", "Staff Room", "Upgrade Room", "Book Room"],
    ["Eternal Slumber", "Book Room", "Hallway", "Staff Room"],
    ["Staff Room", "Feasting Room", "Book Room", "Hallway"],
]

######################################################################
# FUNCTIONS ---------------------------------------


def writeFile():
    """This function writes the map to an external file."""
    global mapFile
    try:
        with open(mapFile, 'w') as file:
            file.write(tabulate(dungeon_map, tablefmt = "grid"))
    except:
        print("An error occurred when writing the file.")
    else:
        print("\n")
        print("You have a map of the dungeon with you.")
    finally:
        print("Use it to your advantage.")
        print("\n")


def readFile():
    """
    This function reads an external file to print the map 
    to the console.
    """
    global mapFile
    try:
        with open(mapFile, 'r') as file:
            print(file.read())
    except:
        print("An error occurred when reading the file.")
    else:
        print("What a useful map.")
    finally:
        print("You continue forward.")
        print("\n")