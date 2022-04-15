# Unit tests for speed conversion
# from the main directory run this command:
#           python -m pytest .\unit_tests\
# Use pip install pytest to install the packages for testing 

#bring in the functions of interest
from turtle import speed
from speed_conversions import *

# Any function that starts with the word 'test' gets run by pytest
def test_all_zeros():
    """
    If the data is all zeros, the the vehicle isn't moving
    and the speed should be exactly zero.
    """
    can_data = b'\x00'*8
    speed_mph = convert_can_bytes_to_speed(can_data)
    assert speed_mph == 0

def test_120kph():
    """
    If the data is all zeros, the the vehicle isn't moving
    and the speed should be exactly zero.
    """
    # 0x78 = 120
    can_data = b'\x00\x00\x78'+b'\x00'*5
    speed_mph = convert_can_bytes_to_speed(can_data)
    #assert speed_mph == 74.5645
    assert speed_mph >=74.56
    assert speed_mph <=74.60

def test_all_FFs():
    """
    All FFs means the data is not available, so no speed value
    should be displayed. The data from this should be None.
    """
    can_data = b'\xFF'*8
    speed_mph = convert_can_bytes_to_speed(can_data)
    assert speed_mph == None

def test_malformed_data():
    """
    Make sure it can handle getting incomplete data without crashing
    """
    can_data = b'\xFF'
    speed_mph = convert_can_bytes_to_speed(can_data)
    assert speed_mph == None

def test_wrong_data_type():
    """
    Make sure it can handle getting the wrong data type
    """
    can_data = 120
    speed_mph = convert_can_bytes_to_speed(can_data)
    assert speed_mph == None