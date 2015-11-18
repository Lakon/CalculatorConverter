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

        inputFormatLabel = tk.Label(self, text="Input Format", anchor='w', fg='black')
        inputFormatLabel.grid(column=0,row=0, columnspan=2, sticky='EW')

        self.inputFormat = tk.StringVar()
        self.inputFormat.set("Two operands")
        self.inputFormatDrop = tk.OptionMenu(self, self.inputFormat, "Two operands", "One operand", "One operand & operator")
        self.inputFormatDrop.grid(column=2,row=0)

        operand1Label = tk.Label(self, text="Operand 1", anchor='w', fg='black')
        operand1Label.grid(column=0,row=1, columnspan=1, sticky='EW')

        base1Label = tk.Label(self, text="Base 1", anchor='w', fg='black')
        base1Label.grid(column=1,row=1, columnspan=1, sticky='EW')

        operatorLabel = tk.Label(self, text="Operator", anchor='w', fg='black')
        operatorLabel.grid(column=2,row=1, columnspan=1, sticky='EW')

        operand2Label = tk.Label(self, text="Operand 2", anchor='w', fg='black')
        operand2Label.grid(column=3,row=1, columnspan=1, sticky='EW')

        base2Label = tk.Label(self, text="Base 2", anchor='w', fg='black')
        base2Label.grid(column=4,row=1, columnspan=1, sticky='EW')

        self.operand1Input = tk.StringVar()
        self.operand1Entry = tk.Entry(self, textvariable=self.operand1Input)
        self.operand1Entry.grid(column=0,row=2,sticky='EW')

        #base1 drop down
        self.base1 = tk.StringVar()
        self.base1.set("Decimal")
        self.base1Drop = tk.OptionMenu(self, self.base1, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.base1Drop.grid(column=1,row=2)

        #operator drop down
        self.operator = tk.StringVar()
        self.operator.set("+")
        self.operatorDrop = tk.OptionMenu(self, self.operator, "+", "-", "/", "*", "AND", "OR", "XOR", "NOR", "NOT", "SHL", "SHR")
        self.operatorDrop.grid(column=2,row=2)

        
        self.operand2Input = tk.StringVar()
        self.operand2Entry = tk.Entry(self, textvariable=self.operand2Input)
        self.operand2Entry.grid(column=3,row=2,sticky='EW')

        #base2 drop down
        self.base2 = tk.StringVar()
        self.base2.set("Decimal")
        self.base2Drop = tk.OptionMenu(self, self.base2, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.base2Drop.grid(column=4,row=2)

        outputFormatLabel = tk.Label(self, text="Output Format", anchor='w', fg='black')
        outputFormatLabel.grid(column=0,row=3, columnspan=2, sticky='EW')

        self.outputFormat = tk.StringVar()
        self.outputFormat.set("Decimal")
        self.outputFormatDrop = tk.OptionMenu(self, self.outputFormat, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.outputFormatDrop.grid(column=2,row=3)

        self.calcButton = tk.Button(self,text="Calculate", command=self.OnCalcButtonClicked)
        self.calcButton.grid(column=4,row=3)

        #operand variables
        self.operand1 = tk.StringVar()
        self.operand2 = tk.StringVar()
        self.result = tk.StringVar()


        self.outputOperand1Label = tk.Label(self, textvariable=self.operand1, relief="ridge", anchor='w', fg='black', bg='grey')
        self.outputOperand1Label.grid(column=0,row=5, columnspan=2, sticky='EW')

        self.outputOperatorLabel = tk.Label(self, textvariable=self.operator, relief="ridge", anchor='w', fg='black')
        self.outputOperatorLabel.grid(column=2,row=5, columnspan=1, sticky='EW')

        self.outputOperand2Label = tk.Label(self, textvariable=self.operand2, relief="ridge", anchor='w', fg='black', bg='grey')
        self.outputOperand2Label.grid(column=3,row=5, columnspan=2, sticky='EW')

        equalLabel = tk.Label(self, text="=", anchor='w', fg='black')
        equalLabel.grid(column=5,row=5, columnspan=1, sticky='EW')

        self.resultLabel = tk.Label(self, textvariable=self.result, relief="ridge", anchor='w', fg='black', bg='grey')
        self.resultLabel.grid(column=6,row=5, columnspan=2, sticky='EW')

        self.clearButton = tk.Button(self,text="Clear", command=self.OnClearButtonClicked)
        self.clearButton.grid(column=2,row=6)

        self.quitButton = tk.Button(self,text="Quit", command=self.Quit)
        self.quitButton.grid(column=4,row=6)

        self.operand1Entry.focus_set()
        self.operand1Entry.selection_range(0, tk.END)

    """
    Purpose:    Handle the main logic for the project. Does something depending on the input.
    Parameters: self
    Return:     Outputs to output boxes
    Example:    click button, convert both inputs, calculate input, output input
    """
    def OnCalcButtonClicked(self):
        
        try:
            operator = Operator.stringToOperator(self.operator.get())
            if operator.isArithmetic:
                operand1 = convert(self.operand1Input.get(), Base.stringToBase(self.base1.get()), Base.decimal) 
                operand2 = convert(self.operand2Input.get(), Base.stringToBase(self.base2.get()), Base.decimal)

                self.operand1.set(convert(str(operand1), Base.decimal, Base.stringToBase(self.outputFormat.get())))
                self.operand2.set(convert(str(operand2), Base.decimal, Base.stringToBase(self.outputFormat.get())))
                self.result.set(convert(str(result(operand1, operand2, operator)), Base.decimal, Base.stringToBase(self.outputFormat.get())))
            else:
                operand1 = convert(self.operand1Input.get(), Base.stringToBase(self.base1.get()), Base.binary)
                operand2 = convert(self.operand2Input.get(), Base.stringToBase(self.base2.get()), Base.binary)

                self.operand1.set(convert(str(operand1), Base.binary, Base.stringToBase(self.outputFormat.get())))
                self.operand2.set(convert(str(operand2), Base.binary, Base.stringToBase(self.outputFormat.get())))
                self.result.set(convert(str(result(operand1, operand2, operator)), Base.binary, Base.stringToBase(self.outputFormat.get())))
        except ValueError as e:
            #message box?
            print (e)


    """
    Purpose:    Handle the main logic for the project. Does something depending on the input.
    Parameters: self
    Return:     Outputs to output boxes
    Example:    click button, all boxes are cleared and focus goes to operand1 input
    """
    def OnClearButtonClicked(self):
        self.operand1.set("")
        self.operand2.set("")
        self.result.set("")
        self.operand1Input.set("")
        self.operand2Input.set("")
        self.operand1Entry.select_clear()
        self.operand2Entry.select_clear()

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







