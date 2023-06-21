'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 06/18/2023
Description: Practical Project Part 02 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
from vegetables_record_model import VegetablesRecord
from data_access import DataStore


class Controller:
    """
    The Controller class handles user actions and interacts with the Model and View components.
    """
    
    r = VegetablesRecord # Create an instance of the VegetablesRecord model
    d = DataStore() # Create an instance of the DataStore for data access operations

    def getAll(self):
        """
        Reloads the data from the dataset by calling the readData() method of the DataStore.
        """
        self.d.readData() 
        print("------DATA RELOADED SUCCESSFULLY------")

    def createNewFile(self):
        """
        Creates a new file for persisting the data by calling the newFile() method of the DataStore.
        """
        self.d.newFile()

    def getRecord(self, input):
        """
        Retrieves and displays the specified record(s) by calling the getRecords() method of the DataStore.
        """
        self.d.getRecords(input)
    
    def insertRecord(self, ref_date, geo, dguid, type_of_product, type_of_storage,
                  uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                  value, status, symbol, terminated, decimals):
        """
        Inserts a new record with the provided data by calling the insertRecords() method of the DataStore.
        """
        self.d.insertRecords(ref_date, geo, dguid, type_of_product, type_of_storage,
                          uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                          value, status, symbol, terminated, decimals)
        print("------NEW RECORD INSERTED SUCCESSFULLY------")

    def updateRecord(self, i, ref_date, geo, dguid, type_of_product, type_of_storage,
                uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                value, status, symbol, terminated, decimals):
        """
        Updates the record at the specified index with the provided data by calling the editRecords() method
        of the DataStore.
        """
        self.d.editRecords(i,ref_date, geo, dguid, type_of_product, type_of_storage,
                             uom, uom_id, scalar_factor, scalar_id, vector,
                             coordinate, value, status, symbol, terminated, decimals)
        print("\n-------EDITED SUCCESSFULLY---------.")

    def deleteRecord(self, d):
        """
        Deletes the record with the specified index by calling the deleteRecords() method of the DataStore.
        """
        self.d.deleteRecords(d)
        print("\n--------DELETED SUCCESSFULLY---------")
        