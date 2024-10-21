import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication
from PyQt5.QtGui import QFont

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Account Registration")

        # Program Title
        self.program_title = QLabel("Account Registration", self)
        self.program_title.setFont(QFont("Arial", 8))
        self.program_title.setFixedHeight(12)

        # Create layout for organized placement
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Labels and Line Edits
        self.info_fields = {}
        y_pos = 10  # Starting position for the first label
        for label_text in ["First Name:", "Last Name:", "Username:", "Password:", "Email Address:", "Contact Number:"]:
            label = QLabel(label_text, self)
            line_edit = QLineEdit(self)
            self.info_fields[label_text] = (label, line_edit)

            # Add label and line edit to the layout with spacing
            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)
            y_pos += 30  # Adjust y position for next element

        # Buttons
        self.submit_button = QPushButton("Submit", self)
        self.clear_button = QPushButton("Clear", self)

        # Add buttons to the layout with spacing
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.clear_button)

        # Functionality for submit button can be added here (e.g., validation, data processing)
        self.submit_button.clicked.connect(self.handle_submit)

        self.clear_button.clicked.connect(self.clear_fields)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clear_fields(self):
        for line_edit in self.info_fields.values():
            line_edit[1].setText("")  # Access line edit through tuple

    def handle_submit(self):
        # Implement logic to handle form submission (e.g., data validation, storing information)
        # Access user input from self.info_fields dictionary
        print("Form submitted with data:")
        for label_text, (label, line_edit) in self.info_fields.items():
            print(f"{label_text}: {line_edit.text()}")

if __name__ == '__main__':
    app = QApplication([])
    ex = RegistrationForm()
    sys.exit(app.exec_())