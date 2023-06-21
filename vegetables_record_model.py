'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 06/18/2023
Description: Practical Project Part 02 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
#We use triple quotation marks for multi-line strings.


class VegetablesRecord:
    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    #We have to use the __init__() function to assign values to object properties, 
    #or other operations that are necessary to do when the object is being created
    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage,
                 uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                 value, status, symbol, terminated, decimals):
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
        return (
            f'{self.ref_date} | {self.geo} | {self.dguid} | {self.type_of_product} | {self.type_of_storage} | '
            f'{self.uom} | {self.uom_id} | {self.scalar_factor} | {self.scalar_id} | {self.vector} | '
            f'{self.coordinate} | {self.value} | {self.status} | {self.symbol} | {self.terminated} | {self.decimals}'
        )    
