import re
from Operator import Operator


"""Algorithm:
            If list length >= 3
                Get operator
                Get first operand
                Get second operand
            If list length == 1
                If there is an operator
                    Get operator
                    Get first operand
                    Get second operand
                Else
                    Get only operand
            Return operands and operator"""
def parse(equation):
    #print(equation)

    #list from command line, but string from terminal prompt
    #my logic needs list for now
    if type(equation) is str:
        equation = [equation]

    operands = []

    #From the command line and it is a full equation with an operator 
    #and two operands. Anything in the list past the third item isn't
    #used and is essentially discarded.
    if len(equation) >= 3:
        operator = getOperator(equation[1])
        if not operator:
            raise ValueError("Invalid equation. No valid operator")

        #split operand into tuple with its base
        if re.fullmatch(r"[dhb]", equation[0][-1], re.IGNORECASE):
            operands.append((equation[0][:-1], equation[0][-1].lower()))
        else:
            operands.append((equation[0], None))

        if re.fullmatch(r"[dhb]", equation[2][-1], re.IGNORECASE):
            operands.append((equation[2][:-1], equation[2][-1].lower()))
        else:
            operands.append((equation[2], None))

    #From the command line or from terminal prompt. It can be a full equation or
    #just one operand. Anything past the second operand is discarded.
    elif len(equation) == 1:
        equation = equation[0]

        operatorPattern = re.compile(r"[+\-\*xX/\\]{1}")
        basePattern = re.compile(r"[dhb]", re.IGNORECASE)

        match = re.search(operatorPattern, equation)

        if match:
            operator = getOperator(match.group(0)) #this should never be None
            assert operator

            operands = [x.strip() for x in equation.split(match.group(0))]

            firstOperand = operands[0]
            secondOperand = operands[1]

            operands = []

            #split operand into tuple with its base
            if re.fullmatch(basePattern, firstOperand[-1]):
                operands.append((firstOperand[:-1], firstOperand[-1].lower()))
            else:
                operands.append((firstOperand, None))

            if re.fullmatch(basePattern, secondOperand[-1]):
                operands.append((secondOperand[:-1], secondOperand[-1].lower()))
            else:
                operands.append((secondOperand, None))

        #Just one operand here
        else:
            operator = None

            #split operand into tuple with its base
            if re.fullmatch(basePattern, equation[-1]):
                operands.append((equation[:-1], equation[-1].lower()))
            else:
                operands.append((equation, None))
    else:
        raise ValueError("Invalid equation")

    return operands, operator


def getOperator(opStr):
    if opStr == '+':
        return Operator.addition
    if opStr == '-':
        return Operator.subtraction
    if opStr == '*' or opStr == 'x' or opStr == 'X':
        return Operator.multiplication
    if opStr == '/' or opStr == '\\':
        return Operator.division
    return None
