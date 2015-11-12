"""
File:         Operator.py
Programmer:   Thomas Martin
Date:         11/12/15
Description:  An enumeration covering each of the operators that our project supports.
              It supports arithmetic operations: addition, subtraction, multiplication, division.
              It supports bitwise operations: AND, OR, XOR (exclusive or), NOR, NOT, SHL (shift left), SHR (shift right).
"""
from enum import Enum

class Operator(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    AND = 5
    OR = 6
    XOR = 7
    NOR = 8
    NOT = 9
    SHL = 10
    SHR = 11

    