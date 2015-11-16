import struct
from Operator import Operator

"""
    File:
    Programmer: Janet Razo
    Date: 11/3/15
    Description:
"""
def Tobin(operand, base, operator):
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
        
    while (operator == '+' or '-' or '*' or '/'):
        if base == 'h':
            num = int(operand, 16)
            return num       
        elif base == 'b':
            num = int(operand, 2)
            return num
        elif base == 'd':
            num = operand
            return num

"""
    File:
    Programmer: Janet Razo
    Date: 11/5/15
    Description:
"""

def Tohex(operand, base, operator):
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
    
    while (operator == '+' or '-' or '*' or '/'):
        if base == 'h':
            num = int(operand, 16)
            return num       
        elif base == 'b':
            num = int(operand, 2)
            return num
        elif base == 'd':
            num = operand
            return num

"""
    File:
    Programmer: Janet Razo
    Date: 11/3/15
    Description:
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
    File:
    Programmer: Janet Razo
    Date: 11/10/15
    Description:
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
    File:
    Programmer: Janet Razo
    Date: 11/13/15
    Description:
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

print(flsem('01000000110101000000000000000000'))           
            
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













