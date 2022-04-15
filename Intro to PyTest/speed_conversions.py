# Example code to convert a CAN message to speed
import struct

def convert_can_bytes_to_speed(can_data):
    """
    The purpose of this function is to produce an number 
    that represents the speed in MPH based on a J1939 message.

    If the conversion fails or the speed is out of bounds, return None.

    The can_data input should be 8 bytes from the J1939 message
    for Cruise Control/Vehice Speed, PGN 65265.
    
    The data is defined as a 16-bit (2 byte) word in Little Endian
    format where the least significant bit represents 1/256 km/h.

    The operating range for the speed is 0 to 250.996

    """
    # Extract the 2 bytes for speed.
    # J1939 specifies bytes 2 and 3 indexed from 1
    # Python indexes from zero and the last index is not included
    speed_bytes = can_data[1:3] 

    #unpack the speed byted to an integer using the struct function
    # See https://docs.python.org/3/library/struct.html#format-characters
    speed_int = struct.unpack("<h",speed_bytes)[0]

    # Convert the integer into km/h
    speed_kph = speed_int/256

    if speed_kph > 250.996:
        return None

    # convert the kph to mph
    speed_mph = speed_kph*0.6213712

    return speed_mph

if __name__ == '__main__':
    can_bytes = b'12345678'
    speed_mph = convert_can_bytes_to_speed(can_bytes)
    print(f"{can_bytes} -> {speed_mph} mph")