from tkinter import *
class MyWindow:
    def __init__(self, win):
            # common widgets
            self.Label1 = Label(win, fg="red", text=("Calculator"))
            self.Label1.place(x=150, y=50)
            self.Label2 = Label(win, fg="green", text=("Number 1:"))
            self.Label2.place(x=50, y=80)
            self.Entry1 = Entry(win, bd=2)
            self.Entry1.place(x=150, y=80)

            self.Label3 = Label(win, fg="green", text=("Number 2:"))
            self.Label3.place(x=50, y=110)
            self.Entry2 = Entry(win, bd=2)
            self.Entry2.place(x=150, y=110)

            self.Label4 = Label(win, fg="green", text=("Result:"))
            self.Label4.place(x=50, y=140)
            self.Entry3 = Entry(win, bd=2)
            self.Entry3.place(x=150, y=140)

            self.Button1 = Button(win, fg="blue", text="Add")
            self.Button1.place(x=80, y=200)
            self.Button1.bind('<Button-1>', self.add)

            self.Button2 = Button(win, fg="blue", text="Subtract")
            self.Button2.place(x=120, y=200)
            self.Button2.bind('<Button-1>', self.subtract)

            self.Button3 = Button(win, fg="blue", text="Multiply")
            self.Button3.place(x=180, y=200)
            self.Button3.bind('<Button-1>', self.multiply)

            self.Button4 = Button(win, fg="blue", text="Divide")
            self.Button4.place(x=240, y=200)
            self.Button4.bind('<Button-1>', self.divide)
    def add(self, win):
            self.Entry3.delete(0, 'end')
            num1 = int(self.Entry1.get())
            num2 = int(self.Entry2.get())
            result = num1 + num2
            self.Entry3.insert(END, str(result))

    def subtract(self,win):
            self.Entry3.delete(0, 'end')
            num1 = int(self.Entry1.get())
            num2 = int(self.Entry2.get())
            result = num1 - num2
            self.Entry3.insert(END, str(result))

    def multiply(self,win):
            self.Entry3.delete(0, 'end')
            num1 = int(self.Entry1.get())
            num2 = int(self.Entry2.get())
            result = num1 * num2
            self.Entry3.insert(END, str(result))

    def divide(self,win):
            self.Entry3.delete(0, 'end')
            num1 = int(self.Entry1.get())
            num2 = int(self.Entry2.get())
            result = num1 / num2
            self.Entry3.insert(END, str(result))

window = Tk()
MyWin = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Special Midterm Exam in OOP")
#window.config(bg="maroon")

window.mainloop()