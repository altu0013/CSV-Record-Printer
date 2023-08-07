'''
Author: Caner Altun - 041025544
Course: CST_8333_350 Programming Language Research
Date: 08/25/2023
Description: Practical Project Part 04 program that uses CSV library to open 
and print records from the CSV dataset on screen.
'''
from data_access import DataStore

def test_readData():
    # Create an instance of the DataStore class
    data_store = DataStore()

    # Call the readData method
    data_store.readData()

    # Assert that the vegetables_dataset list is not empty
    assert len(data_store.vegetables_dataset) != 0

    # Assert that the length of the vegetables_dataset list is correct
    assert len(data_store.vegetables_dataset) == 100

