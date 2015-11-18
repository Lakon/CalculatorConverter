"""
    File:          BaseEquation.py
    Programmer:    Janet Razo
    Date:          11/17/15
    Description:   This file converts the base they input to the base the user wants to output.
"""

import struct
from Base import Base



"""
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""

def convert(operand, inputBase, outputBase):
    if inputBase == Base.decimal:
        if outputBase == Base.decimal:
            num = operand
            return num
        elif outputBase == Base.hexadecimal:
            if '.' in operand:
                return decToHex(operand)
            else:
                return DecToHex(operand) 
        elif outputBase == Base.binary:
            if '.' in operand:
                return decToBin(operand)
            else:
                return DecToBin(operand)
        elif outputBase == Base.sem:
            return binsem(operand)
    elif inputBase == Base.hexadecimal:
        if outputBase == Base.decimal:
            return HexToDec(operand)
        elif outputBase == Base.hexadecimal:
            num = operand
            return num
        elif outputBase == Base.binary:
            return HexToBin(operand)
        elif ouputBase == Base.sem:
            change = HexToDec(operand)
            return binsem(change)
    elif inputBase == Base.binary:
        if outputBase == Base.decimal:
            return BinToDec(operand)
        elif outputBase == Base.hexadecimal:
            return BinToHex(operand)
        elif outputBase == Base.binary:
            num = operand
            return num
        elif outputBase == Base.sem:
            change = BinToDec(operand)
            return binsem(change)
    elif inputBase == Base.sem:
        if outputBase == Base.decimal:
            return flsem(operand)
        elif outputBase == Base.hexadecimal:
            change = flsem(operand)
            if '.' in change:
                return decToHex(change)
            else:
                return DecToHex(change)
        elif outputBase == Base.binary:
            change = flsem(operand)
            if '.' in change:
                return decToBin(change)
            else:
                return DecToBin(change)
        
        

"""
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""
def DecToBin(operand):
    num = bin(int(operand))[2:]
    return num

def HexToBin(operand):
    num = bin(int(operand, 16))[2:]
    return num

def decToBin( n ):
    if '.' in n:
        pL = n.find('.')    # location of point
        integer = n[:pL]    
        fraction = n[pL+1:]
        integer = bin(int(integer))[2:] + '.'
        fraction = float(n) - int( float(n) )
        counter = 5
        while counter != 0 or fraction != 0:
            fraction *= 2
            if fraction >= 1:
                integer = integer + str(int(fraction))
                fraction -= int(fraction)
            else:
                integer = integer + '0'
            counter -= 1
        return integer
    else:
        return bin(int(n))[2:]
    
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
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""
def DecToHex(operand):
    num = hex(int(operand))[2:]
    return num

def BinToHex(operand):
    num = hex(int(operand,2))[2:]
    return num

def decToHex( n ):
    if '.' in n:
        pL = n.find('.')
        integer = n[:pL]
        fraction = n[pL+1:]
        integer = hex(int(integer))[2:] + '.'
        fraction = float(n) - int(float(n))
        counter = 5
        while counter != 0 or fraction != 0:
            fraction *= 2
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
        return integer
    else:
        return hex(int(n))[2:]

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
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""
def HexToDec(operand):
    num = int(operand, 16)
    return num

def BinToDec(operand):
    num = int(operand, 2)
    return num

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
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""

def binsem(num):
    getBin = lambda x: x > 0 and str(bin(int(x)))[2:] or ("-" + str(bin(int(x)))[3:])
    value = struct.unpack('L', struct.pack('f', float(num)))[0]
    operand = getBin(value)
    first = num[0]
    if first != "-":
        oper = '0' + operand
        return oper
    else:
        return operand


"""
    Purpose:    
    Parameters: 
    Return:     
    Example:    
"""

def flsem(num):
    if (num == num[0:31]):
        raise ValueError('input has to be 32bit long', num)
    elif (num == num[0:32]):
        if all(c in '01' for c in num):
            value = bin(int(num, 2))   
            operand = struct.unpack('f', struct.pack('L', int(value, 2)))[0]
            return operand
        else:
            raise ValueError('input has to be binary', num)
    else:
        raise ValueError('input has to be 32bit long', num)
         
            
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

#I have a function called removeInsignificantZeroes in my Calculations.
#At the moment, it only works for binary strings. I'll fix it to work with any
#base so you can use here and remove the extra zeroes. 










