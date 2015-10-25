import argparse
import sys
from ParseEquation import parse

def main(args):
    if args.equation:
        equation = args.equation
    else:
        equation = input('Enter your equation:')

    try:
        operands, operator = parse(equation)
    except ValueError as e:
        print(e)
        sys.exit()
    except Exception as e:
        print ("Invalid equation")
        sys.exit()


    print("Operands:", operands)
    print("Operator:", operator)


    #conversion

    #calculation

    #output




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("equation", nargs='*', 
                        help="The equation of the form '[operand][d or h or b] [operator] [operand][d or h or b]'.\n\
                        If only one operand is given then this will only convert it.")

    args = parser.parse_args()

    main(args)

