'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 08/05/2023
Description: Practical Project Part 04 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
#We use triple quotation marks for multi-line strings.


# Base class representing vegetable records
class VegetablesRecord:
    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage,
                 uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                 value, status, symbol, terminated, decimals):
        # Constructor to initialize the attributes of the class instance
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
    
    # Method to return a string representation of the object
    def __str__(self):
        return (
            f'{self.ref_date} | {self.geo} | {self.dguid} | {self.type_of_product} | {self.type_of_storage} | '
            f'{self.uom} | {self.uom_id} | {self.scalar_factor} | {self.scalar_id} | {self.vector} | '
            f'{self.coordinate} | {self.value} | {self.status} | {self.symbol} | {self.terminated} | {self.decimals}'
        )

# Subclass representing processed vegetable records, inheriting from VegetablesRecord
class ProcessedVegetablesRecord(VegetablesRecord):
    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage,
                 uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                 value, status, symbol, terminated, decimals, process_method):
        # Call the __init__() of the base class to initialize common attributes
        super().__init__(ref_date, geo, dguid, type_of_product, type_of_storage,
                         uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                         value, status, symbol, terminated, decimals)
        self.process_method = process_method  # New attribute for processed vegetables
    
    # Method to return a string representation of the object, including the process method
    def __str__(self):
        base_info = super().__str__()  # Get the base class string representation
        return f'{base_info} | Process Method: {self.process_method}'