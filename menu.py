class Menu:
    def __init__(self, menuOptions):
        self.menuOptions = menuOptions

    def createMenu(self):
        """
        This function creates a menu for the user to choose options
        """
        try:
            print("Now choose your option. ")
            count = 0
            # Loop through list of menu options
            for option in self.menuOptions:
                # Give each listed option an identifier ie 1), 2), 3), etc.
                if count <= len(self.menuOptions):
                    count += 1
                    print(f"{count}) {option}") # Print options
            # User input to choose direction, only allows index number
            optionChoice = int(input("Please choose a NUMBER: "))
            # Return the direction option chosen from the list
            return self.menuOptions[optionChoice-1]
        except Exception:
            print("There was an error. Read instructions carefully and check your input.")


# Create menu objects
# List of movement options for main menu
menuMain = Menu(["Move", "View Map", "Check Inventory", "Quit"])
# List of direction options for sub menu
menuSub = Menu(["Up", "Down", "Left", "Right", "Search The Area", "Back", "Quit"])