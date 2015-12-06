"""
Filename:     Calc_gui.py
Programmer:   Thomas Martin
Date:         11/12/15
Description:  This file holds the class for the gui of our project.
              It will handle the logic; calling convert and calculate when needed and
              print to the output boxes. Has buttons for calculate, clear, and quit.  
"""


import tkinter as tk
import re
import string
from Calculations import result
from BaseEquation import convert
from Operator import Operator
from Base import Base

class CalcConvertApp(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.minsize(width=800, height=200)
        #self.maxsize(width=1600,height=1000)
        self.grid()



        # input operand 1
        self.input_operand1 = tk.StringVar()
        self.input_operand1.trace(mode='w',callback=self.OnInputChanged)

        operand1_InputFrame = tk.Frame(self)
        operand1_InputFrame.grid(column=1,row=0, sticky='WE')

        operand1Label = tk.Label(operand1_InputFrame, width = 32, text="Operand 1", anchor='n', fg='black')
        operand1Label.pack()

        self.operand1Entry = tk.Entry(operand1_InputFrame, textvariable=self.input_operand1)
        self.operand1Entry.pack(fill='x', expand=True)

        self.error1 = tk.StringVar()
        self.operand1_Error = tk.Label(self, textvariable=self.error1, anchor='center', fg='red')
        self.operand1_Error.grid(column=1,row=2, sticky='WE')

        # input operand 2
        self.input_operand2 = tk.StringVar()
        self.input_operand2.trace(mode='w',callback=self.OnInputChanged)

        operand2_InputFrame = tk.Frame(self)
        operand2_InputFrame.grid(column=3,row=0, sticky='WE')

        operand2Label = tk.Label(operand2_InputFrame, width=32, text="Operand 2", anchor='n', fg='black')
        operand2Label.pack()

        self.operand2Entry = tk.Entry(operand2_InputFrame, textvariable=self.input_operand2)
        self.operand2Entry.pack(fill='x', expand=True)


        # error labels
        self.error1 = tk.StringVar()
        self.operand1_Error = tk.Label(self, textvariable=self.error1, anchor='center', fg='red')
        self.operand1_Error.grid(column=1,row=2, sticky='WE')

        self.error2 = tk.StringVar()
        self.operand2_Error = tk.Label(self, textvariable=self.error2, anchor='center', fg='red')
        self.operand2_Error.grid(column=3, row=2, sticky="WE")


        # base 1
        base1Frame = tk.Frame(self)
        base1Frame.grid(column=2,row=0)

        base1Label = tk.Label(base1Frame, text="Base 1", anchor='n', fg='black')
        base1Label.pack()

        self.input_base1 = tk.StringVar()
        self.input_base1.set("Decimal")
        self.input_base1Drop = tk.OptionMenu(base1Frame, self.input_base1, "Decimal", "Hexadecimal", "Binary", "SEM", command=self.OnInputChanged)
        self.input_base1Drop.pack()


        # base 2
        base2Frame = tk.Frame(self)
        base2Frame.grid(column=4,row=0)

        base2Label = tk.Label(base2Frame, text="Base 2", anchor='n', fg='black')
        base2Label.pack()

        self.input_base2 = tk.StringVar()
        self.input_base2.set("Decimal")
        self.input_base2Drop = tk.OptionMenu(base2Frame, self.input_base2, "Decimal", "Hexadecimal", "Binary", "SEM", command=self.OnInputChanged)
        self.input_base2Drop.pack()


        # operator drop down
        operatorFrame = tk.Frame(self)
        operatorFrame.grid(column=2,row=3)

        operatorLabel = tk.Label(operatorFrame, text="Operator", anchor='w', fg='black')
        operatorLabel.pack()

        self.operator = tk.StringVar()
        self.operator.set("+")
        self.operatorDrop = tk.OptionMenu(operatorFrame, self.operator, "+", "-", "/", "*", "AND", "OR", "XOR", "NOR", "NOT", "SHL", "SHR", command=self.OnInputChanged)
        self.operatorDrop.pack()
        


        # operand variables
        self.operand1 = ("", Base.decimal)
        self.operand2 = ("", Base.decimal)
        self.result = ("", Base.decimal)



        self.output_decimalOperand1 = tk.StringVar()
        self.output_decimalOperand2 = tk.StringVar()
        self.output_decimalResult = tk.StringVar()

        self.output_hexOperand1 = tk.StringVar()
        self.output_hexOperand2 = tk.StringVar()
        self.output_hexResult = tk.StringVar()

        self.output_binaryOperand1 = tk.StringVar()
        self.output_binaryOperand2 = tk.StringVar()
        self.output_binaryResult = tk.StringVar()

        self.output_semOperand1 = tk.StringVar()
        self.output_semOperand2 = tk.StringVar()
        self.output_semResult = tk.StringVar()

        

        # output labels
        outputLabelFrame = tk.Frame(self)
        outputLabelFrame.grid(column=0,row=3, columnspan=1, sticky='WE')

        decimalLabel = tk.Label(outputLabelFrame, text="Decimal", anchor='w', fg='black')
        decimalLabel.grid(column=0,row=0, sticky='W')

        hexLabel = tk.Label(outputLabelFrame, text="Hexadecimal", anchor='w', fg='black')
        hexLabel.grid(column=0,row=1, sticky='W')

        binaryLabel = tk.Label(outputLabelFrame, text="Binary", anchor='w', fg='black')
        binaryLabel.grid(column=0,row=2, sticky='W')

        semLabel = tk.Label(outputLabelFrame, text="SEM", anchor='w', fg='black')
        semLabel.grid(column=0,row=3, sticky='W')


        # output operand 1
        operand1_OutputFrame = tk.Frame(self)
        operand1_OutputFrame.grid(column=1,row=3, columnspan=1, sticky='EW')

        self.output_decimalOperand1Label = tk.Label(operand1_OutputFrame, textvariable=self.output_decimalOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_decimalOperand1Label.pack(side = 'top', fill='x')

        self.output_hexOperand1Label = tk.Label(operand1_OutputFrame, textvariable=self.output_hexOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_hexOperand1Label.pack(side ='top', fill='x')

        self.output_binaryOperand1Label = tk.Label(operand1_OutputFrame, textvariable=self.output_binaryOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_binaryOperand1Label.pack(side = 'top', fill='x')

        self.output_semOperand1Label = tk.Label(operand1_OutputFrame, textvariable=self.output_semOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_semOperand1Label.pack(side = 'top', fill='x')

        #output operand 2
        operand2_OutputFrame = tk.Frame(self)
        operand2_OutputFrame.grid(column=3,row=3, columnspan=1, sticky='EW')

        self.output_decimalOperand2Label = tk.Label(operand2_OutputFrame, textvariable=self.output_decimalOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_decimalOperand2Label.pack(side = 'top', fill='x')

        self.output_hexOperand2Label = tk.Label(operand2_OutputFrame, textvariable=self.output_hexOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_hexOperand2Label.pack(side = 'top', fill='x')

        self.output_binaryOperand2Label = tk.Label(operand2_OutputFrame, textvariable=self.output_binaryOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_binaryOperand2Label.pack(side = 'top', fill='x')

        self.output_semOperand2Label = tk.Label(operand2_OutputFrame, textvariable=self.output_semOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_semOperand2Label.pack(side = 'top', fill='x')

        

        # output results
        result_OutputFrame = tk.Frame(self, width = 100)
        result_OutputFrame.grid(column=5,row=3, sticky='WE')

        self.decimalResultLabel = tk.Label(result_OutputFrame, textvariable=self.output_decimalResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.decimalResultLabel.pack(side = 'top', fill='x')

        self.hexResultLabel = tk.Label(result_OutputFrame, textvariable=self.output_hexResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.hexResultLabel.pack(side = 'top', fill='x')

        self.binaryResultLabel = tk.Label(result_OutputFrame, textvariable=self.output_binaryResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.binaryResultLabel.pack(side = 'top', fill='x')

        self.semResultLabel = tk.Label(result_OutputFrame, textvariable=self.output_semResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.semResultLabel.pack(side = 'top', fill='x')


        #equal sign
        equalLabel = tk.Label(self, text="=", anchor='w', fg='black')
        equalLabel.grid(column=4,row=3, columnspan=1)

        resultLabel = tk.Label(self, width=32,text="Result", anchor='n', fg='black')
        resultLabel.grid(column=5,row=0, columnspan=1, sticky='N')

        self.clearButton = tk.Button(self,text="Clear", command=self.OnClearButtonClicked)
        self.clearButton.grid(column=1,row=4)

        self.quitButton = tk.Button(self,text="Quit", command=self.Quit)
        self.quitButton.grid(column=3,row=4)

        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=0)
        self.grid_columnconfigure(5,weight=1)
        self.resizable(True,False)
        #self.update()
        #self.geometry(self.geometry())   


        self.operand1Entry.focus_set()
        self.operand1Entry.selection_range(0, tk.END)



    def OnInputChanged(self, *args): #args just catches tkinter arguments. I don't need them
        #print (args, str(args[0]))
        self.operand1 = (self.input_operand1.get(), Base.stringToBase(self.input_base1.get()))
        self.operand2 = (self.input_operand2.get(), Base.stringToBase(self.input_base2.get()))
        operator = Operator.stringToOperator(self.operator.get())

        isGood = self.canCalculate(operator)
        print ("canCalculate()",isGood)
        if isGood:
            #self.outputResults('1')
            #self.outputResults('2')

            operand1 = convert(self.operand1[0], self.operand1[1], Base.decimal)
            operand2 = convert(self.operand2[0], self.operand2[1], Base.decimal)

            if operator == Operator.DIV and float(operand2) == 0:
                self.outputError('2', "Can't divide by 0")
                self.outputResults('result', clear=True)
                return

            try:
                self.result = (result(operand1, operand2, operator), Base.decimal)
                self.outputResults('result')
            except Exception as e:
                print("Calculation: ", e)
        else:
            self.outputResults('result', clear=True)

        # if   self.operand1[1] == Base.decimal:
        #     try:
        #         float(self.operand1[0])
        #     except:
        #         self.outputError('1',"Invalid input for decimal")
        # elif self.operand1[1] == Base.hexadecimal:
        #     if all(c in string.hexdigits for c in self.operand1[1]):
        #         self.outputError('1',"Invalid input for hexadecimal")
        # elif self.operand1[1] == Base.binary:
        #     if all(c in '01' for c in self.operand1[1]):
        #         self.outputError('1',"Invalid input for binary")
        # else: # Base.sem
        #     if all(c in '01' for c in self.operand1[1]):
        #         self.outputError('1',"Invalid input for SEM")
        #     elif len(self.operand1[0]) != 32:
        #         self.outputError('1',"SEM needs to be 32 bits long")

        # if   self.operand2[1] == Base.decimal:
        #     try:
        #         float(self.operand2[0])
        #     except:
        #         self.outputError('2',"Invalid input for decimal")
        # elif self.operand2[1] == Base.hexadecimal:
        #     if all(c in string.hexdigits for c in self.operand2[1]):
        #         self.outputError('2',"Invalid input for hexadecimal")
        # elif self.operand2[1] == Base.binary:
        #     if all(c in '01' for c in self.operand2[1]):
        #         self.outputError('2',"Invalid input for binary")
        # else: # Base.sem
        #     if all(c in '01' for c in self.operand2[1]):
        #         self.outputError('2',"Invalid input for SEM")
        #     elif len(self.operand2[0]) != 32:
        #         self.outputError('2',"SEM needs to be 32 bits long")


        # if not operator.isArithmetic:
        #     if self.operand1[1] == Base.sem:
        #         self.outputError('1', "Integer only for logical operations")
        #     elif '.' in self.operand1[0]:
        #         self.outputError('1', "Integer only for logical operations")

        # if not operator.isArithmetic:
        #     if self.operand2[1] == Base.sem:
        #         self.outputError('2', "Integer only for logical operations")
        #     elif '.' in self.operand2[0]:
        #         self.outputError('2', "Integer only for logical operations")


        

        # try:
        #     print (self.operand1[0], self.operand2[0])
        #     if self.operand1[0] != "":
        #         try:
        #             self.output_decimalOperand1.set(convert(self.operand1[0], self.operand1[1], Base.decimal))
        #         except ValueError as e:
        #             self.output_decimalOperand1.set(str(e))

        #         try:
        #             self.output_hexOperand1.set(convert(self.operand1[0], self.operand1[1], Base.hexadecimal))
        #         except ValueError as e:
        #             self.output_hexOperand1.set(str(e))

        #         try:
        #             self.output_binaryOperand1.set(convert(self.operand1[0], self.operand1[1], Base.binary))
        #         except ValueError as e:
        #             self.output_binaryOperand1.set(str(e))

        #         try:
        #             self.output_semOperand1.set(convert(self.operand1[0], self.operand1[1], Base.sem))
        #         except ValueError as e:
        #             self.output_semOperand1.set(str(e))
        #     else:
        #         self.output_decimalOperand1.set('')
        #         self.output_hexOperand1.set('')
        #         self.output_binaryOperand1.set('')
        #         self.output_semOperand1.set('')


        #     if self.operand2[0] != "":

        #         try:
        #             self.output_decimalOperand2.set(convert(self.operand2[0], self.operand2[1], Base.decimal))
        #         except ValueError as e:
        #             self.output_decimalOperand2.set(str(e))

        #         try:
        #             self.output_hexOperand2.set(convert(self.operand2[0], self.operand2[1], Base.hexadecimal))
        #         except ValueError as e:
        #             self.output_hexOperand2.set(str(e))

        #         try:
        #             self.output_binaryOperand2.set(convert(self.operand2[0], self.operand2[1], Base.binary))
        #         except ValueError as e:
        #             self.output_binaryOperand2.set(str(e))

        #         try:
        #             self.output_semOperand2.set(convert(self.operand2[0], self.operand2[1], Base.sem))
        #         except ValueError as e:
        #             self.output_semOperand2.set(str(e))
        #     else:
        #         self.output_decimalOperand2.set('')
        #         self.output_hexOperand2.set('')
        #         self.output_binaryOperand2.set('')
        #         self.output_semOperand2.set('')

        #     self.Calculate(None)
        # except Exception as e:
        #     self.outputResults(True)
        #     print(e)

    def canCalculate(self, operator):
        operand1_isGood = self.checkInput(self.operand1, operator, '1')
        operand2_isGood = self.checkInput(self.operand2, operator, '2')


        if not operand1_isGood:
            return False
        if operator == Operator.NOT:
            return True
        if not operand2_isGood:
            return False

        return True

    def checkInput(self, operand, operator, box):
        if operand[0] == "":
            self.outputResults(box, clear=True)
            self.outputError(box, '')
            return False

        if not operator.isArithmetic:
            if operand[1] == Base.sem:
                self.outputError(box, "Integer only for logical operations")
                return False
            elif '.' in operand[0]:
                self.outputError(box, "Integer only for logical operations")
                return False

        if   operand[1] == Base.decimal:
            try:
                float(operand[0])
            except:
                self.outputError(box,"Invalid input for decimal")
                return False
        elif operand[1] == Base.hexadecimal:
            if operand[0] == '-' or any(c == '-' for c in (operand[0][1:] if operand[0][0] == '-' else operand[0])):
                self.outputError(box,"Invalid input for hexadecimal")
                return False
            if len(operand[0].split('.')) > 2:
                self.outputError(box,"Invalid input for hexadecimal")
                return False
            if not all(c in string.hexdigits for c in [x for x in operand[0] if x != '.' and x != '-']):
                self.outputError(box,"Invalid input for hexadecimal")
                return False
        elif operand[1] == Base.binary:
            if operand[0] == '-' or any(c == '-' for c in (operand[0][1:] if operand[0][0] == '-' else operand[0])):
                self.outputError(box,"Invalid input for binary")
                return False
            if len(operand[0].split('.')) > 2:
                self.outputError(box,"Invalid input for binary")
                return False
            if operand[0] == '.' or not all(c in '01' for c in [x for x in operand[0] if x != '.' and x != '-']):
                self.outputError(box,"Invalid input for binary")
                return False
        else: # Base.sem
            if not all(c in '01' for c in operand[0]):
                self.outputError(box,"Invalid input for SEM")
                return False
            elif len(operand[0]) != 32:
                self.outputError(box,"SEM needs to be 32 bits long")
                return False

        self.outputResults(box)
        self.outputError(box,'')
        return True

    def outputError(self, box, outputString):
        if outputString != '':
            self.outputResults(box, clear=True)

        if box == '1':
            self.error1.set(outputString)
        elif box == '2':
            self.error2.set(outputString)


    def outputResults(self, box, clear=False):
        if box == '1':
            if not clear:
                dec = convert(self.operand1[0], self.operand1[1], Base.decimal)
                hexa = convert(self.operand1[0], self.operand1[1], Base.hexadecimal)
                binary = convert(self.operand1[0], self.operand1[1], Base.binary)
                sem = convert(self.operand1[0], self.operand1[1], Base.sem)
            else:
                dec = ''
                hexa = ''
                binary = ''
                sem = ''
            self.output_decimalOperand1.set(dec)
            self.output_hexOperand1.set(hexa)
            self.output_binaryOperand1.set(binary)
            self.output_semOperand1.set(sem)
        elif box == '2':
            if not clear:
                dec = convert(self.operand2[0], self.operand2[1], Base.decimal)
                hexa = convert(self.operand2[0], self.operand2[1], Base.hexadecimal)
                binary = convert(self.operand2[0], self.operand2[1], Base.binary)
                sem = convert(self.operand2[0], self.operand2[1], Base.sem)
            else:
                dec = ''
                hexa = ''
                binary = ''
                sem = ''
            self.output_decimalOperand2.set(dec)
            self.output_hexOperand2.set(hexa)
            self.output_binaryOperand2.set(binary)
            self.output_semOperand2.set(sem)
        elif box == 'result':
            if not clear:
                dec = convert(self.result[0], self.result[1], Base.decimal)
                hexa = convert(self.result[0], self.result[1], Base.hexadecimal)
                binary = convert(self.result[0], self.result[1], Base.binary)
                sem = convert(self.result[0], self.result[1], Base.sem)
            else:
                dec = ''
                hexa = ''
                binary = ''
                sem = ''
            self.output_decimalResult.set(dec)
            self.output_hexResult.set(hexa)
            self.output_binaryResult.set(binary)
            self.output_semResult.set(sem)
        else:
            raise ValueError("box is invalid")

    """
    Purpose:    Handle the main logic for the project. Does something depending on the input.
    Parameters: self
    Return:     Outputs to output boxes
    Example:    click button, all boxes are cleared and focus goes to operand1 input
    """
    def OnClearButtonClicked(self):
        self.operand1 = ("", self.input_base1)
        self.operand2 = ("", self.input_base1)
        self.result = ("", Base.decimal)

        self.operand1Entry.delete(0,'end')
        self.operand2Entry.delete(0,'end')
        # self.output_decimalOperand1.set('')
        # self.output_decimalOperand2.set('')

        # self.output_hexOperand1.set('')
        # self.output_hexOperand2.set('')

        # self.output_binaryOperand1.set('')
        # self.output_binaryOperand2.set('')

        # self.output_semOperand1.set('')
        # self.output_semOperand2.set('')

        

        self.outputResults(True)

        self.operand1Entry.focus_set()
        self.operand1Entry.selection_range(0, tk.END)

    """
    Purpose:    Quit program
    Parameters: self
    Return:     N/A
    Example:    click button, program closes
    """
    def Quit(self):
        self.destroy()







