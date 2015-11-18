"""
Filename:     Calc_gui.py
Programmer:   Thomas Martin
Date:         11/12/15
Description:  This file holds the class for the gui of our project.
              It will handle the logic; calling convert and calculate when needed and
              print to the output boxes. Has buttons for calculate, clear, and quit.  
"""


import tkinter as tk
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
        self.grid()

        # input labels
        operand1Label = tk.Label(self, text="Operand 1", anchor='w', fg='black')
        operand1Label.grid(column=1,row=0, columnspan=1, sticky='EW')

        base1Label = tk.Label(self, text="Base 1", anchor='w', fg='black')
        base1Label.grid(column=2,row=0, columnspan=1, sticky='EW')

        operand2Label = tk.Label(self, text="Operand 2", anchor='w', fg='black')
        operand2Label.grid(column=4,row=0, columnspan=1, sticky='EW')

        base2Label = tk.Label(self, text="Base 2", anchor='w', fg='black')
        base2Label.grid(column=5,row=0, columnspan=1, sticky='EW')


        # input operands
        self.input_operand1 = tk.StringVar()
        self.input_operand1.trace(mode='w',callback=self.OnInputChanged)

        self.operand1Entry = tk.Entry(self, textvariable=self.input_operand1, validate='key', validatecommand=self.InputOkay)
        self.operand1Entry.grid(column=1,row=1,sticky='EW')

        self.input_operand2 = tk.StringVar()
        self.input_operand2.trace(mode='w',callback=self.OnInputChanged)

        self.operand2Entry = tk.Entry(self, textvariable=self.input_operand2, validate='key', validatecommand=self.InputOkay)
        self.operand2Entry.grid(column=4,row=1,sticky='EW')


        # input bases drop down
        self.input_base1 = tk.StringVar()
        self.input_base1.set("Decimal")
        self.input_base1Drop = tk.OptionMenu(self, self.input_base1, "Decimal", "Hexadecimal", "Binary", "SEM", command=self.OnInputChanged)
        self.input_base1Drop.grid(column=2,row=1)

        self.input_base2 = tk.StringVar()
        self.input_base2.set("Decimal")
        self.input_base2Drop = tk.OptionMenu(self, self.input_base2, "Decimal", "Hexadecimal", "Binary", "SEM", command=self.OnInputChanged)
        self.input_base2Drop.grid(column=5,row=1)


        # operator drop down
        operatorLabel = tk.Label(self, text="Operator", anchor='w', fg='black')
        operatorLabel.grid(column=2,row=2, columnspan=1, sticky='EW')

        self.operator = tk.StringVar()
        self.operator.set("+")
        self.operatorDrop = tk.OptionMenu(self, self.operator, "+", "-", "/", "*", "AND", "OR", "XOR", "NOR", "NOT", "SHL", "SHR", command=self.Calculate)
        self.operatorDrop.grid(column=3,row=2)

        

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
        decimalLabel = tk.Label(self, text="Decimal", anchor='w', fg='black')
        decimalLabel.grid(column=0,row=3, columnspan=1, sticky='EW')

        hexLabel = tk.Label(self, text="Hexadecimal", anchor='w', fg='black')
        hexLabel.grid(column=0,row=4, columnspan=1, sticky='EW')

        binaryLabel = tk.Label(self, text="Binary", anchor='w', fg='black')
        binaryLabel.grid(column=0,row=5, columnspan=1, sticky='EW')

        semLabel = tk.Label(self, text="SEM", anchor='w', fg='black')
        semLabel.grid(column=0,row=6, columnspan=1, sticky='EW')

        # output operands DECIMAL
        self.output_decimalOperand1Label = tk.Label(self, textvariable=self.output_decimalOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_decimalOperand1Label.grid(column=1,row=3, columnspan=2, sticky='EW')

        self.output_decimalOperand2Label = tk.Label(self, textvariable=self.output_decimalOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_decimalOperand2Label.grid(column=3,row=3, columnspan=2, sticky='EW')

        self.decimalResultLabel = tk.Label(self, textvariable=self.output_decimalResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.decimalResultLabel.grid(column=6,row=3, columnspan=2, sticky='EW')

        # output operands HEX
        self.output_hexOperand1Label = tk.Label(self, textvariable=self.output_hexOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_hexOperand1Label.grid(column=1,row=4, columnspan=2, sticky='EW')

        self.output_hexOperand2Label = tk.Label(self, textvariable=self.output_hexOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_hexOperand2Label.grid(column=3,row=4, columnspan=2, sticky='EW')

        self.hexResultLabel = tk.Label(self, textvariable=self.output_hexResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.hexResultLabel.grid(column=6,row=4, columnspan=2, sticky='EW')

        # output operands BINARY
        self.output_binaryOperand1Label = tk.Label(self, textvariable=self.output_binaryOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_binaryOperand1Label.grid(column=1,row=5, columnspan=2, sticky='EW')

        self.output_binaryOperand2Label = tk.Label(self, textvariable=self.output_binaryOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_binaryOperand2Label.grid(column=3,row=5, columnspan=2, sticky='EW')

        self.binaryResultLabel = tk.Label(self, textvariable=self.output_binaryResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.binaryResultLabel.grid(column=6,row=5, columnspan=2, sticky='EW')

        # output operands SEM
        self.output_semOperand1Label = tk.Label(self, textvariable=self.output_semOperand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_semOperand1Label.grid(column=1,row=6, columnspan=2, sticky='EW')

        self.output_semOperand2Label = tk.Label(self, textvariable=self.output_semOperand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.output_semOperand2Label.grid(column=3,row=6, columnspan=2, sticky='EW')

        self.semResultLabel = tk.Label(self, textvariable=self.output_semResult, relief="ridge", anchor='w', fg='black', bg='grey')
        self.semResultLabel.grid(column=6,row=6, columnspan=2, sticky='EW')


        # equal sign
        equalLabel = tk.Label(self, text="=", anchor='w', fg='black')
        equalLabel.grid(column=5,row=4, columnspan=1, sticky='EW')


        self.clearButton = tk.Button(self,text="Clear", command=self.OnClearButtonClicked)
        self.clearButton.grid(column=2,row=7)

        self.quitButton = tk.Button(self,text="Quit", command=self.Quit)
        self.quitButton.grid(column=4,row=7)

        self.operand1Entry.focus_set()
        self.operand1Entry.selection_range(0, tk.END)

    def InputOkay(self, *args):
        return True

    def OnInputChanged(self, *args):
        try:
            self.operand1 = (self.input_operand1.get(), Base.stringToBase(self.input_base1.get()))
            self.operand2 = (self.input_operand2.get(), Base.stringToBase(self.input_base2.get()))
            print (self.operand1[0], self.operand2[0])
            if self.operand1[0] != "":
                try:
                    self.output_decimalOperand1.set(convert(self.operand1[0], self.operand1[1], Base.decimal))
                except ValueError as e:
                    self.output_decimalOperand1.set(str(e))

                try:
                    self.output_hexOperand1.set(convert(self.operand1[0], self.operand1[1], Base.hexadecimal))
                except ValueError as e:
                    self.output_hexOperand1.set(str(e))

                try:
                    self.output_binaryOperand1.set(convert(self.operand1[0], self.operand1[1], Base.binary))
                except ValueError as e:
                    self.output_binaryOperand1.set(str(e))

                # try:
                #     self.output_semOperand1.set(convert(self.operand1[0], self.operand1[1], Base.sem))
                # except ValueError as e:
                #     self.output_semOperand1.set(str(e))
            else:
                self.output_decimalOperand1.set('')
                self.output_hexOperand1.set('')
                self.output_binaryOperand1.set('')
                self.output_semOperand1.set('')


            if self.operand2[0] != "":

                try:
                    self.output_decimalOperand2.set(convert(self.operand2[0], self.operand2[1], Base.decimal))
                except ValueError as e:
                    self.output_decimalOperand2.set(str(e))

                try:
                    self.output_hexOperand2.set(convert(self.operand2[0], self.operand2[1], Base.hexadecimal))
                except ValueError as e:
                    self.output_hexOperand2.set(str(e))

                try:
                    self.output_binaryOperand2.set(convert(self.operand2[0], self.operand2[1], Base.binary))
                except ValueError as e:
                    self.output_binaryOperand2.set(str(e))

                # try:
                #     self.output_semOperand2.set(convert(self.operand2[0], self.operand2[1], Base.sem))
                # except ValueError as e:
                #     self.output_semOperand2.set(str(e))
            else:
                self.output_decimalOperand2.set('')
                self.output_hexOperand2.set('')
                self.output_binaryOperand2.set('')
                self.output_semOperand2.set('')

            self.Calculate(None)
        except Exception as e:
            print(e)


    # def OnInputChanged(self, nothing=None):
    #     self.operand1 = (self.input_operand1.get(), Base.stringToBase(self.input_base1.get()))
    #     self.operand2 = (self.input_operand2.get(), Base.stringToBase(self.input_base2.get()))

    #     self.output_decimalOperand1.set(convert(self.operand1[0], self.operand1[1], Base.decimal))
    #     self.output_decimalOperand2.set(convert(self.operand2[0], self.operand2[1], Base.decimal))

    #     self.output_hexOperand1.set(convert(self.operand1[0], self.operand1[1], Base.hexadecimal))
    #     self.output_hexOperand2.set(convert(self.operand2[0], self.operand2[1], Base.hexadecimal))

    #     self.output_binaryOperand1.set(convert(self.operand1[0], self.operand1[1], Base.binary))
    #     self.output_binaryOperand2.set(convert(self.operand2[0], self.operand2[1], Base.binary))

    #     self.output_semOperand1.set(convert(self.operand1[0], self.operand1[1], Base.sem))
    #     self.output_semOperand2.set(convert(self.operand2[0], self.operand2[1], Base.sem))

    #     self.Calculate(None)



    """
    Purpose:    Handle the main logic for the project. Does something depending on the input.
    Parameters: self
    Return:     Outputs to output boxes
    Example:    click button, convert both inputs, calculate input, output input
    """
    def Calculate(self,nothing=None):
        
        try:
            operator = Operator.stringToOperator(self.operator.get())
            if operator.isArithmetic:
                if self.operand1[0] != "" and self.operand2[0] != "":
                    operand1 = convert(self.operand1[0], self.operand1[1], Base.decimal) 
                    operand2 = convert(self.operand2[0], self.operand2[1], Base.decimal)
                    self.result = (result(operand1, operand2, operator), Base.decimal)
                    self.outputResults()
                else:
                    self.outputResults(True)
            else:
                if self.operand1[0] != "" and self.operand2[0] != "":
                    operand1 = convert(self.operand1[0], self.operand1[1], Base.binary) 
                    operand2 = convert(self.operand2[0], self.operand2[1], Base.binary)
                    self.result = (result(operand1, operand2, operator), Base.binary)
                    self.outputResults()
                elif operator == Operator.NOT and self.operand1[0] != "":
                    operand1 = convert(self.operand1[0], self.operand1[1], Base.binary)
                    self.result = (result(operand1, None, operator), Base.binary)
                    self.outputResults()
                elif operator == Operator.NOT and self.operand2[0] != "":
                    operand2 = convert(self.operand2[0], self.operand2[1], Base.binary)
                    self.result = (result(operand2, None, operator), Base.binary)
                    self.outputResults()
                else:
                    self.outputResults(True)

        except Exception as e:
            #message box?
            print (e)

    def outputResults(self, clear=False):
        try:
            if not clear:
                self.output_decimalResult.set(convert(self.result[0], self.result[1], Base.decimal))
                self.output_hexResult.set(convert(self.result[0], self.result[1], Base.hexadecimal))
                self.output_binaryResult.set(convert(self.result[0], self.result[1], Base.binary))
                self.output_semResult.set(convert(self.result[0], self.result[1], Base.sem))
            else:
                self.output_decimalResult.set('')
                self.output_hexResult.set('')
                self.output_binaryResult.set('')
                self.output_semResult.set('')
        except Exception as e:
            print(e)

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







