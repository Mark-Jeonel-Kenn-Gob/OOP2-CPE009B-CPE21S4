from tkinter import *

class MyWindow:
    def __init__(self, win):

            self.Button1 = Button(win, text="Click to Change Color")
            self.Button1.place(x=130, y=130)
            self.Button1.bind('<Button-1>', self.Click)

    def Click(self, win):
        self.Button1.config(bg="yellow")

window = Tk()
MyWin = MyWindow(window)

window.geometry("380x300")
window.title("Special Midterm Exam in OOP")

window.mainloop()