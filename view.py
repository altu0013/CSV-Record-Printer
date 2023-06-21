'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 06/18/2023
Description: Practical Project Part 02 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
from controller import Controller

class View(object):
    """
        The View class handles the user interface and user inputs for interacting with the program.
    """

    def __init__(self):
        self.c = Controller() # Create an instance of the Controller class

    def menu(self):
        """
        Displays the main menu and handles user input for executing different program options.
        """
        
        menu = """
        Program by Caner Altun\n
        1: Reload the data from the dataset, replacing the in-memory data
        2: Persist the data from memory to the disk as a comma-separated file, writing to a new file.
        3: Select and display either one record, or display multiple records from the in-memory data.
        4: Create a new record and store it in the simple data structure in memory
        5: Select and edit a record held in the simple data structure in memory
        6: Select and delete a record from the simple data structure in memory
        7: Exit the program
        """
        print(menu)
        user_input = int(input("Please enter a number between 1-7 to perform one of the menu item: "))


        if user_input == 1:
                # Reload the data from the dataset
                Controller().getAll()
                self.menu()

        elif user_input == 2:
                # Persist the data from memory to the disk as a new CSV file
                Controller().createNewFile()
                self.menu()

        elif user_input == 3:
                # Select and display the specified record(s) from the in-memory data
                display_input = int(input("Which row would you like to display? Enter between 1-100: \n"
                           "Enter 0 for all the records: "))

                Controller().getRecord(display_input)
                self.menu()
                
        elif user_input == 4:
                # Create a new record and store it in the simple data structure in memory
                REF_DATE = str(input("REF_DATE: "))
                GEO = str(input("GEO: "))
                DGUID = str(input("DGUID: "))
                TYPE_OF_PRODUCT = str(input("Type of Product: "))
                TYPE_OF_STORAGE = str(input("Type of Storage: "))
                UOM = str(input("UOM: "))
                UOM_ID = str(input("UOM ID: "))
                SCALAR_FACTOR = str(input("Scalar Factor: "))
                SCALAR_ID = str(input("Scalar ID: "))
                VECTOR = str(input("Vector: "))
                COORDINATE = str(input("Coordinate: "))
                VALUE = str(input("Value: "))
                STATUS = str(input("Status: "))
                SYMBOL = str(input("Symbol: "))
                TERMINATED = str(input("Terminated: "))
                DECIMALS = str(input("Decimals: "))
                 # Call the insertRecord() method of the Controller
                Controller().insertRecord(REF_DATE, GEO, DGUID, TYPE_OF_PRODUCT, TYPE_OF_STORAGE, UOM, UOM_ID,
                               SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE,
                               STATUS, SYMBOL, TERMINATED, DECIMALS)
                self.menu()         
                                
        elif user_input == 5:
                # Prompt user for updated values of the record fields and store them in variables
                selectedRow = int(input("Please enter the row number you need to update (0-100): "))
                edit_REF_DATE = str(input("New REF_DATE: "))
                edit_GEO = str(input("New GEO: "))
                edit_DGUID = str(input("New DGUID: "))
                edit_TYPE_OF_PRODUCT = str(input("New Type of Product: "))
                edit_TYPE_OF_STORAGE = str(input("New Type of Storage: "))
                edit_UOM = str(input("New UOM: "))
                edit_UOM_ID = str(input("New UOM ID: "))
                edit_SCALAR_FACTOR = str(input("New Scalar Factor: "))
                edit_SCALAR_ID = str(input("New Scalar ID: "))
                edit_VECTOR = str(input("New Vector: "))
                edit_COORDINATE = str(input("New Coordinate: "))
                edit_VALUE = str(input("New Value: "))
                edit_STATUS = str(input("New Status: "))
                edit_SYMBOL = str(input("New Symbol: "))
                edit_TERMINATED = str(input("New Terminated: "))
                edit_DECIMALS = str(input("New Decimals: "))
                # Call the updateRecord() method of the Controller
                Controller().updateRecord(selectedRow, edit_REF_DATE, edit_GEO, edit_DGUID, edit_TYPE_OF_PRODUCT, edit_TYPE_OF_STORAGE, 
                                     edit_UOM, edit_UOM_ID, edit_SCALAR_FACTOR, edit_SCALAR_ID, edit_VECTOR, edit_COORDINATE, 
                                     edit_VALUE, edit_STATUS, edit_SYMBOL, edit_TERMINATED, edit_DECIMALS)
                self.menu()

        elif user_input == 6:
                deleteRow = int(input("Which row would you like to delete? Please enter row number: "))
                Controller().deleteRecord(deleteRow) # Call the deleteRecord() method of the Controller
                self.menu()
            
        elif user_input == 7:
                print("\n-------EXITING------\nThank you for using the program.\nProgram by Caner Altun\n")
                exit()
        else:
               print("\n--------INVALID VALUE--------")
               self.menu()


