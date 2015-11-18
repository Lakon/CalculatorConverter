"""
File:         Base.py
Programmer:   Thomas Martin
Date:         11/12/15
Description:  An enumeration covering each of the bases that our project supports.
              It supports decimal, hexadecimal, binary, and SEM (sign exponent mantissa).
"""

from enum import Enum

class Base(Enum):
    decimal = 1
    hexadecimal = 2
    binary = 3
    sem = 4

    def stringToBase(b):
        if b == 'Decimal':
            return Base.decimal
        if b == 'Hexadecimal':
            return Base.hexadecimal
        if b == 'Binary':
            return Base.binary
        if b == 'SEM':
            return Base.sem
        raise ValueError("invalid base")
    