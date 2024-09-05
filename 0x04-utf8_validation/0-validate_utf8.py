#!/usr/bin/python3
"""
    Module implementing a function that checks if given set of characters
    are UTF-8 encoding valid

"""
from typing import List


def validUTF8(data: List) -> bool:
    """Checks if given data or dataset is utf8-encoding valid"""
    num_bytes = 0

    masks = [
            0b10000000,
            0b11100000,
            0b11110000,
            0b11111000
            ]

    values = [
            0b00000000,
            0b11000000,
            0b11100000,
            0b11110000
            ]

    for num in data:
        byte = num & 0xFF
        if num_bytes == 0:
            if (byte & masks[0] == values[0]):
                num_bytes = 1
            elif (byte & masks[1] == values[1]):
                num_bytes = 2
            elif (byte & masks[2] == values[2]):
                num_bytes = 3
            elif (byte & masks[3] == values[3]):
                num_bytes = 4
            else:
                return False
            num_bytes -= 1
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes -= 1
    return num_bytes == 0
