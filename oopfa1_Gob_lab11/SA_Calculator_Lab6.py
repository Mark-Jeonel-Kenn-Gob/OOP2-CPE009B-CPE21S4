import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setWindowIcon(QIcon("pythonico.ico"))
        self.setGeometry(300, 300, 400, 400)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(50)

        self._create_layout()
        self._create_menu()

        self.history = []

    def _create_layout(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        grid_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('C', 4, 0), ('^', 4, 1), ('sin', 4, 2), ('cos', 4, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, text=text: self.on_button_click(text))
            grid_layout.addWidget(button, row, col)

        layout.addWidget(self.result_display)
        layout.addLayout(grid_layout)

        self.setCentralWidget(central_widget)

    def _create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        save_action = QAction("Save History", self)
        save_action.triggered.connect(self.save_history)
        file_menu.addAction(save_action)

        load_action = QAction("Load History", self)
        load_action.triggered.connect(self.load_history)
        file_menu.addAction(load_action)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.result_display.clear()
        elif button_text == '=':
            self.calculate_result()
        elif button_text in ('sin', 'cos'):
            self.calculate_trig(button_text)
        else:
            current_text = self.result_display.text()
            new_text = current_text + button_text
            self.result_display.setText(new_text)

    def calculate_result(self):
        try:
            expression = self.result_display.text().replace("^", "**")  # Replace ^ with **
            result = eval(expression)
            self.result_display.setText(str(result))
            self.history.append(f"{expression} = {result}")
        except Exception as e:
            self.result_display.setText("Error")

    def calculate_trig(self, operation):
        try:
            expression = self.result_display.text()
            angle = float(expression)
            if operation == 'sin':
                result = math.sin(math.radians(angle))
            elif operation == 'cos':
                result = math.cos(math.radians(angle))
            self.result_display.setText(str(result))
            self.history.append(f"{operation}({angle}) = {result}")
        except Exception as e:
            self.result_display.setText("Error")

    def save_history(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save History", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                for entry in self.history:
                    file.write(entry + '\n')

    def load_history(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Load History", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r') as file:
                history = file.readlines()
                self.result_display.setText("".join(history))

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())