#!/usr/bin/env python3

import argparse
import sys
#from ParseEquation import parse
from Calc_gui import CalcConvertApp

def main():
    # if args.equation:
    #     equation = args.equation
    # else:
    #     equation = input('Enter your equation:')

    # try:
    #     operands, operator = parse(equation)
    # except ValueError as e:
    #     print(e)
    #     sys.exit()
    # except Exception as e:
    #     print ("Invalid equation")
    #     sys.exit()


    # print("Operands:", operands)
    # print("Operator:", operator)

    gui = CalcConvertApp(None)
    gui.title("Calculator Converter")
    gui.mainloop()






if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("equation", nargs='*', 
    #                     help="The equation of the form '[operand][d or h or b] [operator] [operand][d or h or b]'.\n\
    #                     If only one operand is given then this will only convert it.")

    # args = parser.parse_args()

    main()

