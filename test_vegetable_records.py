import pytest
from vegetables_record_model import VegetablesRecord, ProcessedVegetablesRecord

def test_vegetables_record_instantiation():
    # Test creating an instance of VegetablesRecord
    record = VegetablesRecord("2023-07-22", "Canada", "123456", "Carrot", "Cold Storage",
                              "Kg", "kg123", "1.0", "123", "X1", "123.45",
                              "100", "Available", "$", "No", "2")
    
    assert isinstance(record, VegetablesRecord)
    assert record.ref_date == "2023-07-22"
    assert record.geo == "Canada"
    assert record.dguid == "123456"
    # Add more assertions for other attributes

def test_processed_vegetables_record_instantiation():
    # Test creating an instance of ProcessedVegetablesRecord
    record = ProcessedVegetablesRecord("2023-07-22", "Canada", "123456", "Carrot", "Cold Storage",
                                       "Kg", "kg123", "1.0", "123", "X1", "123.45",
                                       "100", "Available", "$", "No", "2", "Chopped")
    
    assert isinstance(record, VegetablesRecord)  # Polymorphism test
    assert isinstance(record, ProcessedVegetablesRecord)
    assert record.ref_date == "2023-07-22"
    assert record.geo == "Canada"
    assert record.dguid == "123456"
    assert record.process_method == "Chopped"
    # Add more assertions for other attributes

def test_polymorphism_with_base_class_list():
    # Test polymorphism by creating a list of base class and subclass instances
    records = [
        VegetablesRecord("2023-07-22", "Canada", "123456", "Carrot", "Cold Storage",
                         "Kg", "kg123", "1.0", "123", "X1", "123.45",
                         "100", "Available", "$", "No", "2"),
        ProcessedVegetablesRecord("2023-07-23", "USA", "789012", "Tomato", "Room Temperature",
                                  "Kg", "kg456", "1.0", "456", "X2", "456.78",
                                  "200", "Out of Stock", "$$", "Yes", "3", "Pureed")
    ]
    
    assert isinstance(records[0], VegetablesRecord)
    assert isinstance(records[1], VegetablesRecord)  # Polymorphism test
    assert isinstance(records[1], ProcessedVegetablesRecord)

if __name__ == "__main__":
    pytest.main()