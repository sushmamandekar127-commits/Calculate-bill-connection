
from calculate_bill_connection_type_unit import calculate_bill

def test_domestic():
    assert calculate_bill("domestic", 100) == 350

def test_commercial():
    assert calculate_bill("commercial", 100) == 700

def test_industrial():
    assert calculate_bill("industrial", 100) == 1000

def test_invalid():
    assert calculate_bill("wrong", 100) == None
