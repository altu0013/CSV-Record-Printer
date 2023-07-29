'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 06/18/2023
Description: Practical Project Part 02 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
#In the next line, csv module is imported. 
#The csv module implements classes to read and write tabular data in CSV format.
import csv
from vegetables_record_model import VegetablesRecord, ProcessedVegetablesRecord
from tabulate import tabulate

# The DataStore class stores and manages the vegetable records.
class DataStore:
    def __init__(self):
        self.vegetables_dataset = [] # List to hold the vegetable records
        self.vegetablesRecord = VegetablesRecord # Reference to the base class for vegetable records

    def readData(self):
        '''
        Reads data from a CSV file and populates the vegetables_dataset list with VegetablesRecord objects.

        Raises:
            FileNotFoundError: If the file is not found.
            IOError: If the file cannot be opened.
        
        Program by Caner Altun
        '''
        try:
            with open("./32100260.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                # Skip the first row (column names)
                next(csv_reader)
                print("\nCaner Altun")
                for index, row in enumerate(csv_reader):
                    # Create a new VegetablesRecord object from the CSV row data
                    vegetables = self.vegetablesRecord(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                        row[8],row[9],row[10],row[11],row[12],row[13], row[14],row[15]
                    )
                    if index < 100:
                        self.vegetables_dataset.append(vegetables) # Add the record to the list
                    else:
                        break # Limit to reading 100 records
                
            # Exception triggered if the file is not found.
        except FileNotFoundError:
            print("File not found, please make sure to enter exact file name")

        # Exception triggered if the file cannot be opened.
        except IOError:
            print("File cannot be opened")
        # The code block within the finally block is always executed regardless of whether an exception occurred or not.
        finally:
            print("\n")

    def newFile(self):
        '''
        Creates a new CSV file and writes the data from the vegetables_dataset list into it.

        Raises:
            IOError: If the file cannot be opened or written.
        '''
        fileName = str(input("Please enter a name for the new file: "))
        try:
            with open(fileName + ".csv", "w", newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(
                    [
                        "ref_date", "geo", "dguid", "type_of_product", "type_of_storage",
                        "uom", "uom_id", "scalar_factor", "scalar_id", "vector", "coordinate",
                        "value", "status", "symbol", "terminated", "decimals",
                    ]
                )

                for record in self.vegetables_dataset:
                    # Write each record's attributes to the new CSV file
                    csv_writer.writerow(
                        [record.ref_date, record.geo, record.dguid, record.type_of_product,
                         record.type_of_storage, record.uom, record.uom_id, record.scalar_factor,
                         record.scalar_id, record.vector, record.coordinate, record.value,
                         record.status,  record.symbol, record.terminated, record.decimals,
                        ]
                    )

            print("\n------NEW CSV FILE CREATED! PLEASE CHECK YOUR FOLDER------\n")

        except IOError:
            print("File cannot be opened or written.")
        finally:
            print("\n")



    def getRecords(self, input):
        '''
        Retrieves and prints records from the vegetables_dataset list based on the provided input.

        Args:
            input (int): The input value to determine which records to print.

        '''
        table_data = []
        headers = [
                "Ref Date", "Geo", "DGUID", "Type of Product", "Type of Storage", "UOM", "UOM ID", "Scalar Factor",
                "Scalar ID", "Vector", "Coordinate", "Value", "Status", "Symbol", "Terminated", "Decimals", "Processed Method"
            ]
        for record in self.vegetables_dataset:
            table_data.append(str(record).split(" | "))

        if input > 100 or input < 0:
            print("---------PLEASE SELECT BETWEEN 0 AND 100---------")

        elif input == 0:
            print(tabulate(table_data, headers, tablefmt="pipe")) # Print all records in a tabulated format

        else: 
            print("---------YOU SELECTED ROW BELOW---------\n")
            print(self.vegetables_dataset[input - 1]) # Print the selected record

    def insertRecords( self, ref_date, geo, dguid, type_of_product, type_of_storage,
                   uom, uom_id, scalar_factor, scalar_id, vector, coordinate, 
                   value, status, symbol, terminated, decimals, process_method=None
    ):
        '''
        Inserts a new record into the vegetables_dataset list.

        Args:
            ref_date (str): The reference date of the record.
            geo (str): The geographical location of the record.
            dguid (str): The data guide of the record.
            type_of_product (str): The type of product.
            type_of_storage (str): The type of storage.
            uom (str): The unit of measurement.
            uom_id (str): The unit of measurement ID.
            scalar_factor (str): The scalar factor.
            scalar_id (str): The scalar ID.
            vector (str): The vector value.
            coordinate (str): The coordinate value.
            value (str): The data value.
            status (str): The status of the record.
            symbol (str): The symbol.
            terminated (str): The termination status.
            decimals (str): The decimal value.
            process_method (str): The process method for processed vegetables (optional).

        '''
        if process_method:
            new_record = ProcessedVegetablesRecord(ref_date, geo, dguid, type_of_product, type_of_storage,
                                                   uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                                                   value, status, symbol, terminated, decimals, process_method)
        else:
            new_record = VegetablesRecord(ref_date, geo, dguid, type_of_product, type_of_storage,
                                          uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                                          value, status, symbol, terminated, decimals)
        self.vegetables_dataset.append(new_record) # Add the new record to the dataset

    def editRecords(self, row, ref_date, geo, dguid, type_of_product,
                      type_of_storage, uom, uom_id, scalar_factor, scalar_id,
                      vector, coordinate, value, status, symbol, terminated, decimals,
    ):
        '''
        Edits an existing record in the vegetables_dataset list.

        Args:
            row (int): The row index of the record to edit.
            ref_date (str): The updated reference date of the record.
            geo (str): The updated geographical location of the record.
            dguid (str): The updated data guide of the record.
            type_of_product (str): The updated type of product.
            type_of_storage (str): The updated type of storage.
            uom (str): The updated unit of measurement.
            uom_id (str): The updated unit of measurement ID.
            scalar_factor (str): The updated scalar factor.
            scalar_id (str): The updated scalar ID.
            vector (str): The updated vector value.
            coordinate (str): The updated coordinate value.
            value (str): The updated data value.
            status (str): The updated status of the record.
            symbol (str): The updated symbol.
            terminated (str): The updated termination status.
            decimals (str): The updated decimal value.

        '''
        self.vegetables_dataset[row - 1] = VegetablesRecord(ref_date, geo, dguid, type_of_product, type_of_storage,
                                                            uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                                                            value, status, symbol, terminated, decimals,
        )

    def deleteRecords(self, row):
        '''
        Deletes a record from the vegetables_dataset list.

        Args:
            row (int): The row index of the record to delete.

        '''
        del self.vegetables_dataset[row - 1]
