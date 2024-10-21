from tkinter import *

class RegistrationWindow:
  def __init__(self, root):
    self.root = root
    self.root.title("Account Registration")

    self.program_title = Label(self.root, text="Account Registration System", font=("Arial", 18))
    self.program_title.grid(row=0, columnspan=2, pady=10)

    self.label_fields = [
      ("First Name:", StringVar()),
      ("Last Name:", StringVar()),
      ("Username:", StringVar()),
      ("Password:", StringVar()),
      ("Email Address:", StringVar()),
      ("Contact Number:", StringVar()),
    ]
    self.entry_widgets = {}
    current_row = 1
    for label_text, variable in self.label_fields:
      label = Label(self.root, text=label_text)
      label.grid(row=current_row, column=0, sticky=W)
      entry = Entry(self.root, textvariable=variable)
      entry.grid(row=current_row, column=1, padx=10)
      self.entry_widgets[label_text] = entry
      current_row += 1

    # Buttons
    self.submit_button = Button(self.root, text="Submit", command=self.submit_registration)
    self.submit_button.grid(row=current_row, column=0, pady=10, padx=10, sticky=E)

    self.clear_button = Button(self.root, text="Clear", command=self.clear_fields)
    self.clear_button.grid(row=current_row, column=1, pady=10, padx=10, sticky=W)

    self.center_window()

  def center_window(self):
    window_width = self.root.winfo_screenwidth()
    window_height = self.root.winfo_screenheight()
    window_x = (window_width / 2) - (self.root.winfo_width() / 2)
    window_y = (window_height / 2) - (self.root.winfo_height() / 2)
    self.root.geometry(f"+{int(window_x)}+{int(window_y)}")

  def submit_registration(self):

    pass

  def clear_fields(self):
    for variable in self.label_fields:
      variable[1].set("")

if __name__ == "__main__":
  root = Tk()
  registration_window = RegistrationWindow(root)
  root.mainloop()
