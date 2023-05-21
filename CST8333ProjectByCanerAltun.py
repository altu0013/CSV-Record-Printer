'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 05/20/2023
Description: Practical Project Part 01 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
#We use triple quotation marks for multi-line strings.

#In the next line, csv module is imported. 
#The csv module implements classes to read and write tabular data in CSV format.
import csv

#Caner Altun
#VegetablesRecord class to create objects representing the data in each row of the CSV file. 
#https://www.w3schools.com/python/python_classes.asp
class VegetablesRecord:
    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    #We have to use the __init__() function to assign values to object properties, 
    #or other operations that are necessary to do when the object is being created
    def __init__(
        self,
        ref_date,
        geo,
        dguid,
        type_of_product,
        type_of_storage,
        uom,
        uom_id,
        scalar_factor,
        scalar_id,
        vector,
        coordinate,
        value,
        status,
        symbol,
        terminated,
        decimals
    ):
        self.ref_date = ref_date
        self.geo = geo
        self.dguid = dguid
        self.type_of_product = type_of_product
        self.type_of_storage = type_of_storage
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals
    
    #Caner Altun
    #The __str__() function returns a string representation of the VegetablesRecord object.
    #https://note.nkmk.me/en/python-long-string/
    def __str__(self):
        return f'{self.ref_date} | {self.geo} | {self.dguid} | {self.type_of_product} | {self.type_of_storage} | {self.uom} | {self.uom_id} |'\
               f'{self.scalar_factor} | {self.scalar_id} | {self.vector} | {self.coordinate} | {self.value} | {self.status} | {self.symbol} | {self.terminated} | {self.decimals}'

#Caner Altun
#The code is enclosed in a try block to handle any potential exceptions that may occur during execution.
try: 
  with open("./32100260.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #Skip the first row (column names)
    next(csv_reader)
    print("\nCaner Altun")
    vegetables_dataset = []

    for row in csv_reader:   
        vegetables = VegetablesRecord(row[0], row[1], row[2],row[3], row[4],row[5],
                                      row[6],row[7], row[8],row[9],row[10],row[11],
                                      row[12],row[13],row[14],row[15])

        vegetables_dataset.append(vegetables)
        
    #Printing rows until row number 200 since there are too many rows in the dataset
    for list_print in range(200):

       print("\n", vegetables_dataset[list_print])

#Exception triggered if the file is not found.
except FileNotFoundError:
    print("File not found, please make sure to enter exact file name")

#Exception triggered if the file cannot be opened.
except IOError:
    print("File cannot be opened")
#The code block within the finally block is always executed regardless of whether an exception occurred or not.
finally:
   print("\nCaner Altun\n")