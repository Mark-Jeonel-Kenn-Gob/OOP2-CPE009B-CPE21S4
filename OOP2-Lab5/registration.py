import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QGridLayout, QMessageBox, QVBoxLayout, QHBoxLayout)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Account Registration")
        self.setGeometry(100, 100, 400, 350)

        main_layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title_label = QLabel("Account Registration")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_layout.addStretch()
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        form_layout = QGridLayout()

        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.email_label = QLabel("Email Address:")
        self.email_input = QLineEdit()
        self.contact_label = QLabel("Contact Number:")
        self.contact_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear")

        self.submit_button.clicked.connect(self.submit_form)
        self.clear_button.clicked.connect(self.clear_form)

        form_layout.addWidget(self.first_name_label, 0, 0)
        form_layout.addWidget(self.first_name_input, 0, 1)
        form_layout.addWidget(self.last_name_label, 1, 0)
        form_layout.addWidget(self.last_name_input, 1, 1)
        form_layout.addWidget(self.username_label, 2, 0)
        form_layout.addWidget(self.username_input, 2, 1)
        form_layout.addWidget(self.password_label, 3, 0)
        form_layout.addWidget(self.password_input, 3, 1)
        form_layout.addWidget(self.email_label, 4, 0)
        form_layout.addWidget(self.email_input, 4, 1)
        form_layout.addWidget(self.contact_label, 5, 0)
        form_layout.addWidget(self.contact_input, 5, 1)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch()
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(title_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def submit_form(self):
        missing_fields = []
        if not self.first_name_input.text():
            missing_fields.append("First Name")
        if not self.last_name_input.text():
            missing_fields.append("Last Name")
        if not self.username_input.text():
            missing_fields.append("Username")
        if not self.password_input.text():
            missing_fields.append("Password")
        if not self.email_input.text():
            missing_fields.append("Email Address")
        if not self.contact_input.text():
            missing_fields.append("Contact Number")

        if missing_fields:
            QMessageBox.warning(self, "Input Error", f"Please fill in the following fields: {', '.join(missing_fields)}.")
            return

        self.save_to_csv()

        self.clear_form()

        QMessageBox.information(self, "Success", "Registration successful!")

    def save_to_csv(self):
        data = [
            self.first_name_input.text(),
            self.last_name_input.text(),
            self.username_input.text(),
            self.password_input.text(),
            self.email_input.text(),
            self.contact_input.text()
        ]

        with open('registrations.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def clear_form(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.contact_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())