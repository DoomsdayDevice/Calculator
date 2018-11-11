from tkinter import *
import inspect

##myFile = open("logs.txt")
##print(myFile.read())

class Calc (Frame):
    """creates a frame inside the window"""
    def __init__ (self, base):
        Frame.__init__(self, base)
        base.geometry("305x450")
        self.grid()
       # self.muhLabel = Label(self, text = "Hello Bitches!")
        self.createWidgets()
        self.updateText()
    def createWidgets(self):
        """creates the current number field"""
        # current number field
        #has to have numbers and the sign
        self.currNumb = DoubleVar()
        self.currNumb = 0
        self.currOpMemo = None
        self.pointIsPressed = False
        self.currentNumber = Text(self, width = 35, height = 1)
        self.currentNumber.grid(row = 0, column = 0, columnspan = 4,
                                padx = 10, pady = 10)

        #current operation field, set as a variable, label updates automatically
        self.currentOp = StringVar()
        self.currentOp.set("")
        self.currOp = IntVar()

        Label(self, textvariable = self.currentOp).grid(row = 1, column = 0,
                                                        columnspan = 4,
                                                        padx = 5, pady = 5, sticky = E)

        #the "clear" button
        self.clearButt = Button(self, text = "C", command = self.clearFields,
                                height = 3, width = 17)
        self.clearButt.grid(row = 3, column = 0, pady = 6, padx = 2, columnspan = 2)


        #divide
        self.divideButt = Button(self, text = ":", command = self.divide,
                                height = 3, width = 6)
        self.divideButt.grid(row = 3, column = 2, pady = 10, padx = 10)
        #multiply
        self.multiButt = Button(self, text = "X", command = self.multiply,
                                height = 3, width = 6)
        self.multiButt.grid(row = 3, column = 3, pady = 10, padx = 10)
        #add
        self.addButt = Button(self, text = "+", command = self.add,
                                height = 8, width = 6)
        self.addButt.grid(row = 5, column = 3, pady = 10, padx = 10, rowspan = 2)
        #subtract
        self.subtractButt = Button(self, text = "-", command = self.subtract,
                                height = 3, width = 6)
        self.subtractButt.grid(row = 4, column = 3, pady = 6, padx = 2)




        #change sign
        self.signButt = Button(self, text = "-/+", command = self.changeSign,
                                height = 3, width = 6)
        self.signButt.grid(row = 7, column = 2, pady = 6, padx = 2)
        #point sign
        self.pointButt = Button(self, text = ".", command = self.point,
                                height = 3, width = 6)
        self.pointButt.grid(row = 7, column = 1, pady = 10, padx = 10)
        #equal sign
        self.equalButt = Button(self, text = "=", command = self.equal,
                                height = 3, width = 6)
        self.equalButt.grid(row = 7, column = 3, pady = 10, padx = 10)



        #digits from 0 to 9
        self.digitZero = Button(self, text = "0", command = self.pressZero,
                                height = 3, width = 6)
        self.digitZero.grid(row = 7, column = 0, pady = 6, padx = 2)
        #1
        self.digitOne = Button(self, text = "1", command = self.pressOne,
                                height = 3, width = 6)
        self.digitOne.grid(row = 4, column = 0, pady = 6, padx = 2)
        #2
        self.digitTwo = Button(self, text = "2", command = self.pressTwo,
                                height = 3, width = 6)
        self.digitTwo.grid(row = 4, column = 1, pady = 6, padx = 2)

        #3
        self.digitThree = Button(self, text = "3", command = self.pressThree,
                                height = 3, width = 6)
        self.digitThree.grid(row = 4, column = 2, pady = 6, padx = 2)

        #4
        self.digitFour = Button(self, text = "4", command = self.pressFour,
                                height = 3, width = 6)
        self.digitFour.grid(row = 5, column = 0, pady = 6, padx = 2)

        #5
        self.digitFive = Button(self, text = "5", command = self.pressFive,
                                height = 3, width = 6)
        self.digitFive.grid(row = 5, column = 1, pady = 6, padx = 2)

        #6
        self.digitSix = Button(self, text = "6", command = self.pressSix,
                                height = 3, width = 6)
        self.digitSix.grid(row = 5, column = 2, pady = 6, padx = 2)

        #7
        self.digitSeven = Button(self, text = "7", command = self.pressSeven,
                                height = 3, width = 6)
        self.digitSeven.grid(row = 6, column = 0, pady = 6, padx = 2)

        #8
        self.digitEight = Button(self, text = "8", command = self.pressEight,
                                height = 3, width = 6)
        self.digitEight.grid(row = 6, column = 1, pady = 6, padx = 2)
        #9
        self.digitNine = Button(self, text = "9", command = self.pressNine,
                                height = 3, width = 6)
        self.digitNine.grid(row = 6, column = 2, pady = 6, padx = 2)

    def clearFields(self):
        self.currentNumber.delete(0.0, END)
        self.currentOp.set("")
        self.currNumb = 0
        self.currOpMemo = None
        self.unPoint()


    def changeSign(self):
        # changes the sign of the current number
        if self.currNumb < 0:
            self.currNumb = abs(self.currNumb)
        else:
            self.currNumb = 0 - self.currNumb
        self.updateText()


    def point(self):
        self.pointIsPressed = True
        self.pointButt.config(bg="grey")


    def unPoint(self):
        self.pointIsPressed = False
        self.pointButt.config(bg="SystemButtonFace")
        ##        print("unpointed")


    def updateText(self):
        # updates text in the number field
        self.currentNumber.delete(0.0, END)
        self.currentNumber.insert(0.0, str(self.currNumb))


    def pressOne(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".1")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "1")
        else:
            self.currNumb = self.currNumb * 10 + 1
        self.updateText()


    def pressTwo(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".2")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "2")
        else:
            self.currNumb = self.currNumb * 10 + 2
        self.updateText()


    def pressThree(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".3")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "3")
        else:
            self.currNumb = self.currNumb * 10 + 3
        self.updateText()


    def pressFour(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".4")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "4")
        else:
            self.currNumb = self.currNumb * 10 + 4
        self.updateText()


    def pressFive(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".5")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "5")
        else:
            self.currNumb = self.currNumb * 10 + 5
        self.updateText()


    def pressSix(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".6")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "6")
        else:
            self.currNumb = self.currNumb * 10 + 6
        self.updateText()


    def pressSeven(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".7")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "7")
        else:
            self.currNumb = self.currNumb * 10 + 7
        self.updateText()


    def pressEight(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".8")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "8")
        else:
            self.currNumb = self.currNumb * 10 + 8
        self.updateText()


    def pressNine(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".9")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "9")
        else:
            self.currNumb = self.currNumb * 10 + 9
        self.updateText()


    def pressZero(self):
        if self.pointIsPressed and float(self.currNumb).is_integer():
            self.currNumb = float(str(self.currNumb) + ".0")
        elif self.pointIsPressed:
            self.currNumb = float(str(self.currNumb) + "0")
        else:
            self.currNumb = self.currNumb * 10 + 0
        self.updateText()


    def divide(self):
        if self.currOpMemo == None:
            self.currOpMemo = self.currNumb
            self.currentOp.set(str(self.currNumb) + " : ")
            self.currSign = ":"
            self.currNumb = 0
            self.unPoint()
        else:
            self.equal()


    def multiply(self):
        if self.currOpMemo == None:
            self.currOpMemo = self.currNumb
            self.currentOp.set(str(self.currNumb) + " X ")
            self.currSign = "x"
            self.currNumb = 0
            self.unPoint()
        else:
            self.equal()


    def add(self):
        if self.currOpMemo == None:
            self.currOpMemo = self.currNumb
            self.currentOp.set(str(self.currNumb) + " + ")
            self.currSign = "+"
            self.currNumb = 0
            self.unPoint()
        else:
            self.equal()


    def subtract(self):
        if self.currOpMemo == None:
            self.currOpMemo = self.currNumb
            self.currentOp.set(str(self.currNumb) + " - ")
            self.currSign = "-"
            self.currNumb = 0
            self.unPoint()
        else:
            self.equal()


    def equal(self):
        if self.currSign == ":":
            self.currOpMemo = self.currOpMemo / self.currNumb
        elif self.currSign == "x":
            self.currOpMemo = self.currOpMemo * self.currNumb
        elif self.currSign == "+":
            self.currOpMemo = self.currOpMemo + self.currNumb
        elif self.currSign == "-":
            self.currOpMemo = self.currOpMemo - self.currNumb
        self.currentOp.set(self.currentOp.get() + str(self.currNumb) + " = " + str(self.currOpMemo))
        self.currOpMemo = None
        self.currNumb = 0
        self.unPoint()

myBase = Tk()
myBase.title("SkyNet v1.0")
myBase.resizable(False, False)
myCalc = Calc(myBase)
myBase.mainloop()
