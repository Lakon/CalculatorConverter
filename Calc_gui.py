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
        self.minsize(width=700, height=200)
        #self.maxsize(width=1600,height=1000)
        self.grid()



        # input operand 1
        self.input_operand1 = tk.StringVar()
        self.input_operand1.trace(mode='w',callback=self.OnInputChanged)

        operand1_InputFrame = tk.Frame(self)
        operand1_InputFrame.grid(column=1,row=0, sticky='WE')

        operand1Label = tk.Label(operand1_InputFrame, text="Operand 1", anchor='w', fg='black')
        operand1Label.pack()

        self.operand1Entry = tk.Entry(operand1_InputFrame, textvariable=self.input_operand1, validate='key', validatecommand=self.InputOkay)
        self.operand1Entry.pack(fill='x', expand=True)


        # input operand 2
        self.input_operand2 = tk.StringVar()
        self.input_operand2.trace(mode='w',callback=self.OnInputChanged)

        operand2_InputFrame = tk.Frame(self)
        operand2_InputFrame.grid(column=3,row=0, sticky='WE')

        operand2Label = tk.Label(operand2_InputFrame, text="Operand 2", anchor='w', fg='black')
        operand2Label.pack()

        self.operand2Entry = tk.Entry(operand2_InputFrame, textvariable=self.input_operand2, validate='key', validatecommand=self.InputOkay)
        self.operand2Entry.pack(fill='x', expand=True)


        # base 1
        base1Frame = tk.Frame(self)
        base1Frame.grid(column=2,row=0)

        base1Label = tk.Label(base1Frame, text="Base 1", anchor='w', fg='black')
        base1Label.pack()

        self.input_base1 = tk.StringVar()
        self.input_base1.set("Decimal")
        self.input_base1Drop = tk.OptionMenu(base1Frame, self.input_base1, "Decimal", "Hexadecimal", "Binary", "SEM", command=self.OnInputChanged)
        self.input_base1Drop.pack()


        # base 2
        base2Frame = tk.Frame(self)
        base2Frame.grid(column=4,row=0)

        base2Label = tk.Label(base2Frame, text="Base 2", anchor='w', fg='black')
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
        self.operatorDrop = tk.OptionMenu(operatorFrame, self.operator, "+", "-", "/", "*", "AND", "OR", "XOR", "NOR", "NOT", "SHL", "SHR", command=self.Calculate)
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

        resultLabel = tk.Label(self, width=20,text="Result", anchor='n', fg='black')
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

                try:
                    self.output_semOperand1.set(convert(self.operand1[0], self.operand1[1], Base.sem))
                except ValueError as e:
                    self.output_semOperand1.set(str(e))
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

                try:
                    self.output_semOperand2.set(convert(self.operand2[0], self.operand2[1], Base.sem))
                except ValueError as e:
                    self.output_semOperand2.set(str(e))
            else:
                self.output_decimalOperand2.set('')
                self.output_hexOperand2.set('')
                self.output_binaryOperand2.set('')
                self.output_semOperand2.set('')

            self.Calculate(None)
        except Exception as e:
            print(e)



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







