"""
File:         Calculations.py
Programmer:   Jose Daniel Velazco
Date:         10/25/15
Description:  Peforms the arithmetic and logical calculations required by our calculator.
              Arithmetic calculations included: Addion, Subtraction, Multiplication, Division
              Logical calculations included: AND, OR, XOR, NOR, NOT, SHR, SHL 
"""
from Operator import Operator

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Logic to this file. Selects appropriate function to run
    Parameter:  Two operands and one operator
    Return:     result from specified calculation
    Example:    5 + 7 yields an output of 12
"""
def result( operandOne, operandTwo, operator ):
    if operator == Operator.ADD:
        return str(float(operandOne) + float(operandTwo))
    elif operator == Operator.SUB:
        return str(float(operandOne) - float(operandTwo))
    elif operator == Operator.MUL:
        return str(float(operandOne) * float(operandTwo))
    elif operator == Operator.DIV:
        return str(float(operandOne) / float(operandTwo))   
    if operator == Operator.NOT:
        return str(~int(operandOne))   
    if operator == Operator.AND:
        print( int(operandOne) & int(operandTwo) )
        return str(int(operandOne) & int(operandTwo))       
    elif operator == Operator.OR:
        return str(int(operandOne) | int(operandTwo))
    elif operator == Operator.XOR:
        return str( int(operandOne) ^ int(operandTwo))
    elif operator == Operator.NOR:
        return str(~(int(operandOne) | int(operandTwo)))
    elif operator == Operator.SHL:
        return str(int( operandOne ) << int( operandTwo ))
    elif operator == Operator.SHR:
        return str(int( operandOne ) >> int( operandTwo ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def normalize( num ):
    isNegative = False
    print( num )
    if '-' == num[0]:
        num = num[1:]
        isNegative = True
    if 'e+' in num:          # for large numbers
        num = num[::-1]     # reverses string
        exponent = ''
        while num[0] != '+':    # finds exponent number
            exponent = exponent + num[0]
            num = num[1:]
        exponent = exponent[::-1]
        num = num[2:]       # revmoes e+
        num = num[::-1]     # reverses string back to normal
        exponent = int(exponent)
        if '.' in num:      # if it has fraction
            exponent = exponent - len(num) + 2
            num = num[0] + num[2:]  # removes dot
            num = num + '0'*exponent # adds the 0's
        else:
            num = num + '0'*exponent # adds the 0's
        if isNegative:
            num = '-' + num
        print(num)
        return num
    
    elif 'e-' in num:        # for small numbers
        num = num[::-1]     # reverses string
        exponent = ''
        while num[0] != '-':    # finds exponent number
            exponent = exponent + num[0]
            num = num[1:]
        exponent = exponent[::-1]
        num = num[2:]       # revmoes e-
        num = num[::-1]     # reverses string back to normal
        exponent = int(exponent) - 1
        if '.' in num:
            num = num[0] + num[2:]  # removes the dot
        num = '0.' + '0'*exponent + num
        if isNegative:
            num = '-' + num
        return num
    else:
        return num
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Remove all insignificant zeroes from a string of binary numbers
    Parameter:  Binary number as a string
    Return:     Simplified binary number as a string
    Example:    input of "001101.01100" yields an output of "1101.011"
"""
def removeInsignificantZeroes( number ):
    if number == "0":
        return "0"
    while True: 
        if number[0] == '0' and number[1] != '.':
            number = number[1:]
        else:
            break
    number = number[::-1]  #reverses the string
    while True:
        if number[0] == '0' and number[1] != '.':
            number = number[1:]
        else:
            break
    number = number[::-1]
    if number == "0.0":
        return "0"
    else:
        return number
    
#~~~~~~~~~~~~~~~~~~~~~~ Following code is not used ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Perform bitwise NOT operator to a binary number in string form
    Parameter:  One binary number in string form
    Return:     result binary number in string form
    Example:    input of "1011.11" yields an output of "100"
"""
def logicalNOT( operand ):
    result = ''
    for i in range(len(operand)):
        if operand[i] == '1':
            result = result + '0'
        elif operand[i] == '0':
            result = result + '1'
        elif operand[i] == '.':
            result = result + '.'
    return removeInsignificantZeroes( result )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Perform bitwise XOR operator to two binary numbers in string form
    Parameter:  Two binary numbers in string form
    Return:     result binary number in string form
    Example:    input of "1011.11" and "10.01101' yields an output of "1001.10101"
"""
def logicalXOR( operandOne, operandTwo):
    if '.' in operandOne or '.' in operandTwo:
        operandOne, operandTwo = equalLen( operandOne, operandTwo)        
        result = ''
        for i in range( len(operandOne) ):
            if operandOne[i] == '1' and operandTwo[i] == '1':
                result = result + '0'
            elif operandOne[i] == '0' and operandTwo[i] == '0':
                result = result + '0'
            elif operandOne[i] == '.':
                result = result + '.'
            else:
                result = result + '1'
        return removeInsignificantZeroes(result)
    else:
        return bin( int(operandOne,2) & int(operandTwo,2))[2:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Perform bitwise OR operator to two binary numbers in string form
    Parameter:  Two binary numbers in string form
    Return:     result binary number in string form
    Example:    input of "1011.11" and "10.01101' yields an output of "100.0001"
"""
def logicalNOR( operandOne, operandTwo):
    if '.' in operandOne or '.' in operandTwo:
        operandOne, operandTwo = equalLen( operandOne, operandTwo)        
        result = ''
        for i in range( len(operandOne) ):
            if operandOne[i] == '1' or operandTwo[i] == '1':
                result = result + '0'
            elif operandOne[i] == '.':
                result = result + '.'
            else:
                result = result + '1'
        return removeInsignificantZeroes(result)
    else:
        return bin( int(operandOne,2) & int(operandTwo,2))[2:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Perform bitwise AND operator to two binary numbers in string form
    Parameter:  Two binary numbers in string form
    Return:     result binary number in string form
    Example:    input of "1011.11" and "10.01101' yields an output of "10.01"
"""
def logicalAND( operandOne, operandTwo):
    result = ''
    for i in range( len(operandOne) ):
        if operandOne[i] == '1' and operandTwo[i] == '1':
            result = result + '1'
        else:
            result = result + '0'
    return result
##    if '.' in operandOne or '.' in operandTwo:
##        operandOne, operandTwo = equalLen( operandOne, operandTwo)        
##        result = ''
##        for i in range( len(operandOne) ):
##            if operandOne[i] == '1' and operandTwo[i] == '1':
##                result = result + '1'
##            elif operandOne[i] == '.':
##                result = result + '.'
##            else:
##                result = result + '0'
##        return removeInsignificantZeroes(result)
##    else:
##        return bin( int(operandOne,2) & int(operandTwo,2))[2:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Perform bitwise OR operator to two binary numbers in string form
    Parameter:  Two binary numbers in string form
    Return:     result binary number in string form
    Example:    input of "1011.11" and "10.01101' yields an output of "1011.11101"
"""
def logicalOR( operandOne, operandTwo):
    if '.' in operandOne or '.' in operandTwo:
        operandOne, operandTwo = equalLen( operandOne, operandTwo)        
        result = ''
        for i in range( len(operandOne) ):
            if operandOne[i] == '1' or operandTwo[i] == '1':
                result = result + '1'
            elif operandOne[i] == '.':
                result = result + '.'
            else:
                result = result + '0'
        return removeInsignificantZeroes(result)
    else:
        return bin( int(operandOne,2) | int(operandTwo,2))[2:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
    Purpose:    Turns two binary numbers of string type and make themo of equal length
              by adding insignificant zeros. 
    Parameter:  Two binary numbers as string
    Return:     Tuple with equal length strings
    Example:    input of "101.1" and "11.0101" yields the tuple ("101.1000", "011.0101")
"""
def equalLen( operandOne, operandTwo):
    integer1 = 0
    fractional1 = 0
    integer2 = 0
    fractional2 = 0

    integer1 = operandOne.find('.')
    if integer1 == -1:
        operandOne = operandOne + '.'
        integer1 = operandOne.index('.')
    fractional1  = len(operandOne) - integer1 - 1

    integer2 = operandTwo.find('.')
    if integer2 == -1:
        operandTwo = operandTwo + '.'
        integer2 = operandTwo.index('.')
    fractional2 = len(operandTwo) - integer2 - 1

    if integer1 < integer2:
        operandOne = '0'*(integer2 - integer1) + operandOne
    else:
        operandTwo = '0'*(integer1 - integer2) + operandTwo

    if fractional1 < fractional2:
        operandOne = operandOne + '0'*(fractional2 - fractional1)
    else:
        operandTwo = operandTwo + '0'*(fractional1 - fractional2)
    return (operandOne, operandTwo)


  

