"""
    File:          BaseEquation.py
    Programmer:    Janet Razo
    Date:          11/19/15
    Description:   This file converts the base the user input to the base the user
                   wants to output and also has the sem conversion.
"""

import struct
from Base import Base
from Calculations import removeInsignificantZeroes
from Calculations import normalize
from Operator import Operator




"""
    Purpose:    Selects the method depending on the user input and want they want
                to output.
    Parameters: The operand, the base input by the user, and the output base the user wants
    Return:     outputs a base or sem depending what the user specifies
    Example:    10 decimal to hexadecimal outputs a
"""

def convert(operand, inputBase, outputBase):
    #correct edge case of having only a decimal before the num
    if '.' in operand:
        idx = operand.index('.')
        if idx == 0:
            operand = '0' + operand[idx:]
        elif idx == 1 and operand[0] == '-':
            operand = '-0' + operand[1:]

    # input is Decimal
    if inputBase == Base.decimal:
        if outputBase == Base.decimal:
            return operand
        elif outputBase == Base.hexadecimal:
            return decToHex(operand)
        elif outputBase == Base.binary:
            return decToBin(operand)
        elif outputBase == Base.sem:
            return binsem(operand)

    #input is Hex
    elif inputBase == Base.hexadecimal:
        if outputBase == Base.decimal:
            return hexToDec(operand)
        elif outputBase == Base.hexadecimal:
            return operand
        elif outputBase == Base.binary:
            return hexToBin(operand)
        elif outputBase == Base.sem:
            return binsem(hexToDec(operand))

    # input is Binary
    elif inputBase == Base.binary:
        if outputBase == Base.decimal:
            return binToDec(operand)
        elif outputBase == Base.hexadecimal:
            return binToHex(operand)
        elif outputBase == Base.binary:
            return operand
        elif outputBase == Base.sem:
            return binsem(binToDec(operand))

    #input is SEM
    elif inputBase == Base.sem:
        if outputBase == Base.decimal:
            return flsem(operand)
        elif outputBase == Base.hexadecimal:
            return decToHex(normalize(flsem(operand)))
        elif outputBase == Base.binary:
            return decToBin(normalize(flsem(operand)))
        elif outputBase == Base.sem:
            return operand
        
        

"""
    Parameters: The input operand
    Return:     Each method will return a binary number
    Example:    B hexadecimal will output 1011
"""
# def DecToBin(operand):
#     num = bin(int(operand))[2:]
#     return num

# def HexToBin(operand):
#     num = bin(int(operand, 16))[2:]
#     return num

def decToBin( n ):
    isNegative = False
    if n[0] == '-':
        isNegative = True
        n = n[1:]
    if '.' in n:
        pL = n.find('.')    # location of point
        integer = n[:pL]    
        fraction = n[pL+1:]
        integer = bin(int(integer))[2:] + '.'
        fraction = float(n) - int( float(n) )
        counter = 32
        while counter > 0 and fraction != 0:
            fraction *= 2
            if fraction >= 1:
                integer = integer + str(int(fraction))
                fraction -= int(fraction)
            else:
                integer = integer + '0'
            counter -= 1
        num = removeInsignificantZeroes(integer)
        return ('-' + num) if isNegative else num
    else:
        b = bin(int(n))[2:]
        return ('-' + b) if isNegative else b
    
"""
def Tobin(operand):
    if base == 'h':
        num = bin(int(operand, 16))[2:]
        return num       
    elif base == 'b':
        num = (operand)
        return num
    elif base == 'd':
        num = bin(int(operand))[2:]
        return num
    else:
        raise ValueError('that base is not allowed', base)
"""     
#----------------------------------------    

"""
    Parameters: The input operand
    Return:     Each method will return a hexadecimal number
    Example:    1100 binary will output C  
"""
def DecToHex(operand):
    num = hex(int(operand))[2:]
    return num

def BinToHex(operand):
    num = hex(int(operand,2))[2:]
    return num

def decToHex( n ):
    isNegative = False
    if n[0] == '-':
        isNegative = True
        n = n[1:]
    if '.' in n:
        pL = n.find('.')
        integer = n[:pL]
        fraction = n[pL+1:]
        integer = hex(int(integer))[2:] + '.'
        fraction = float(n) - int(float(n))
        counter = 32
        while counter != 0 and fraction != 0:
            fraction *= 16
            if fraction >= 1:
                if int(fraction) == 10:
                    integer = integer + 'a'
                elif int(fraction) == 11:
                    integer = integer + 'b'
                elif int(fraction) == 12:
                    integer = integer + 'c'
                elif int(fraction) == 13:
                    integer = integer + 'd'
                elif int(fraction) == 14:
                    integer = integer + 'e'
                elif int(fraction) == 15:
                    integer = integer + 'f'
                elif int(fraction) <= 9:
                    integer = integer + str(int(fraction))
                fraction -= int(fraction)
            else:
                integer = integer + '0'
            counter -= 1
        num = removeInsignificantZeroes(integer)
        return ('-'+num) if isNegative else num
    else:
        h = hex(int(n))[2:]
        return ('-' + h) if isNegative else h

"""
def Tohex(operand):
    if base == 'h':
        num = operand
        return num       
    elif base == 'b':
        num = hex(int(operand,2))[2:]
        return num
    elif base == 'd':
        num = hex(int(operand))[2:]
        return num
    else:
        raise ValueError('that base is not allowed', base)
"""    
#-------------------------------------   

"""
    Parameters: The input operand
    Return:     Each method will return a decimal number
    Example:    1010 hexadecimal will output 10    
"""
def HexToDec(operand):
    num = int(operand, 16)
    convert = str(num)
    return convert

def BinToDec(operand):
    num = int(operand, 2)
    convert = str(num)
    return convert

def hexToDec(operand):
    isNegative = False
    if operand[0] == '-':
        isNegative = True
        operand = operand[1:]
    if '.' in operand:
        locate = operand.find('.')
        first = operand[:locate]
        last = operand[locate+1:]
        integer = HexToDec(first) + '.'
        n = 0
        move = 0
        for x in last:
            if x == 'a':
                move += (10*16**(n-1))
            elif x == 'b':
                move += (11*16**(n-1))
            elif x == 'c':
                move += (12*16**(n-1))
            elif x == 'd':
                move += (13*16**(n-1))
            elif x == 'e':
                move += (14*16**(n-1))
            elif x == 'f':
                move += (15*16**(n-1))
            else:
                change = float(x)
                move += (change*16**(n-1))
            n -= 1
        num = float(integer) + move
        convert = str(num)
        return ('-' + convert) if isNegative else convert
    else:
        d = str(int(operand, 16))
        return ('-' + d) if isNegative else d

def binToDec(operand):        
    isNegative = False
    if operand[0] == '-':
        isNegative = True
        operand = operand[1:]
    if '.' in operand:
        locate = operand.find('.')
        first = operand[:locate]
        last = operand[locate+1:]
        integer = BinToDec(first) + '.'
        move = 0
        n = 0
        for x in last:
            change = float(x)
            move += (change*2**(n-1))
            n -= 1
        num = float(integer) + move
        convert = str(num)
        return ('-' + convert) if isNegative else convert
    else:
        d = str(int(operand,2))
        return ('-' + d) if isNegative else d

def binToHex(operand):           
    dec = binToDec(operand)
    convert = decToHex(dec)
    return convert

def hexToBin(operand):          
    dec = hexToDec(operand)
    convert = decToBin(dec)
    return convert

"""
def Todec(operand, base):
    if base == 'h':
        num = int(operand, 16)
        return num       
    elif base == 'b':
        num = int(operand, 2)
        return num
    elif base == 'd':
        num = operand
        return num
    else:
        raise ValueError('that base is not allowed', base)
"""
#-------------------------------------------

"""
    Parameters: The input operand
    Return:     will return a sem value
    Example:    3.0 float will output 01000000110101000000000000000000    
"""

def binsem(num):
    getBin = lambda x: x > 0 and str(bin(int(x)))[2:] or ("-" + str(bin(int(x)))[3:])
    value = struct.unpack('=L', struct.pack('=f', float(num)))[0]
    operand = getBin(value)
    first = num[0]
    if first != "-":
        return '0' + operand
    else:
        return operand


"""
    Parameters: The input operand
    Return:     will return a float value
    Example:    01000000110101000000000000000000 sem will output 3.0    
"""

def flsem(num):
    value = bin(int(num, 2))   
    operand = str(struct.unpack('=f', struct.pack('=L', int(value, 2)))[0])
    return operand
         
"""  
def floatsem(num):
    sign = 0
    exponent = 0
    mantissa = 0
    first = num[0]
    eight = num[1:9]
    rest = num[9:32]
    if first == 1:
        sign = '-'
        num = -num
    for i in range(len(eight)):
        if eight[i] == '1':
            exponent = exponent + 1
    for i in range(len(rest)):
        if rest[i] == '1':
            mantissa = mantissa + 1/2
    return (sign, exponent, mantissa)
"""    










