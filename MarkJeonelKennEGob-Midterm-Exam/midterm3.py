from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.Label1 = Label(win, fg="red", text=("Enter your fullname:"))
        self.Label1.place(x=50, y=80)
        self.Entry1 = Entry(win, bd=6, width=35)
        self.Entry1.place(x=275, y=80)


        self.Button1 = Button(win, fg="red", text="Click to display your Fullname")
        self.Button1.place(x=50, y=120)
        self.Button1.bind('<Button-1>', self.Click)
        self.Entry2 = Entry(win, bd=6, width=35)
        self.Entry2.place(x=275, y=120)

    def Click(self, win):
        self.Entry2.delete(0, 'end')
        num1 = str(self.Entry1.get())
        result = num1
        self.Entry2.insert(END, str(result))

window = Tk()
MyWin = MyWindow(window)

window.geometry("550x280")
window.title("Midterm in OOP")

window.mainloop()