from tkinter import *

__author__ = 'sci-lmw1'

""" CP1200 2015 SP1 Demo. Lindsay Ward, 19/05/2015
    GUI with list of buttons
"""

INITIAL_WELCOME = "Welcome. Enter name:"

class App():
    def __init__(self):
        self.window = Tk()
        self.window.title("CP1200 Demo")
        self.introLabel = Label(self.window, text=INITIAL_WELCOME)
        self.introLabel.pack()
        self.nameEntry = Entry(self.window)
        self.nameEntry.pack()
        self.checkButton = Button(self.window, text="Check", command=self.checkName)
        self.checkButton.pack()
        self.statusLabel = Label(self.window, text="")
        self.statusLabel.pack()
        self.buttonList = []
        for i in range(10):
            # lambda function used to pass value to function
            # see http://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-loop-with-lambda
            # for why we need the "number=i" part
            self.buttonList.append(Button(self.window, text=str(i), command=lambda number=i: self.pressNumberButton(number)))
            self.buttonList[i].pack(side="left")
        mainloop()

    def checkName(self):
        name = self.nameEntry.get()
        if name.strip() == "":
            self.statusLabel["text"] = "Invalid name"
            self.introLabel["text"] = INITIAL_WELCOME

        else:
            self.introLabel["text"] = "Welcome " + name
            self.statusLabel["text"] = ""

    def pressNumberButton(self, number):
        # print(number)
        self.buttonList[number]["text"] = "X"


def main():
    App()

main()

