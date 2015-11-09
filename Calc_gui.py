import tkinter as tk

class CalcConvertApp(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        inputFormatLabel = tk.Label(self, text="Input Format", anchor='w', fg='black', bg='grey')
        inputFormatLabel.grid(column=0,row=0, columnspan=2, sticky='EW')

        self.inputFormat = tk.StringVar()
        self.inputFormat.set("Two operands")
        self.inputFormatDrop = tk.OptionMenu(self, self.inputFormat, "Two operands", "One operand", "One operand & operator")
        self.inputFormatDrop.grid(column=2,row=0)

        operand1Label = tk.Label(self, text="Operand 1", anchor='w', fg='black', bg='grey')
        operand1Label.grid(column=0,row=1, columnspan=1, sticky='EW')

        base1Label = tk.Label(self, text="Base 1", anchor='w', fg='black', bg='grey')
        base1Label.grid(column=1,row=1, columnspan=1, sticky='EW')

        operatorLabel = tk.Label(self, text="Operator", anchor='w', fg='black', bg='grey')
        operatorLabel.grid(column=2,row=1, columnspan=1, sticky='EW')

        operand2Label = tk.Label(self, text="Operand 2", anchor='w', fg='black', bg='grey')
        operand2Label.grid(column=3,row=1, columnspan=1, sticky='EW')

        base2Label = tk.Label(self, text="Base 2", anchor='w', fg='black', bg='grey')
        base2Label.grid(column=4,row=1, columnspan=1, sticky='EW')

        self.operand1Entry = tk.Entry(self)
        self.operand1Entry.grid(column=0,row=2,sticky='EW')

        #base1 drop down
        self.base1 = tk.StringVar()
        self.base1.set("Decimal")
        self.base1Drop = tk.OptionMenu(self, self.base1, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.base1Drop.grid(column=1,row=2)

        #operator drop down
        self.operator = tk.StringVar()
        self.operator.set("+")
        self.operatorDrop = tk.OptionMenu(self, self.operator, "+", "-", "/", "*")
        self.operatorDrop.grid(column=2,row=2)

        self.operand2Entry = tk.Entry(self)
        self.operand2Entry.grid(column=3,row=2,sticky='EW')

        #base2 drop down
        self.base2 = tk.StringVar()
        self.base2.set("Decimal")
        self.base2Drop = tk.OptionMenu(self, self.base2, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.base2Drop.grid(column=4,row=2)

        outputFormatLabel = tk.Label(self, text="Output Format", anchor='w', fg='black', bg='grey')
        outputFormatLabel.grid(column=0,row=3, columnspan=2, sticky='EW')

        self.outputFormat = tk.StringVar()
        self.outputFormat.set("Decimal")
        self.outputFormatDrop = tk.OptionMenu(self, self.outputFormat, "Decimal", "Hexadecimal", "Binary", "SEM")
        self.outputFormatDrop.grid(column=2,row=3)

        self.calcButton = tk.Button(self,text="Calculate")
        self.calcButton.grid(column=4,row=3)



