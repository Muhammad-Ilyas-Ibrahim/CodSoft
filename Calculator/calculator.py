import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from time import sleep

class CalculatorButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(60, 60)
        self.setStyleSheet(
            "QPushButton {"
            "   background-color: #f0f0f0;"
            "   border: 2px solid #d0d0d0;"
            "   border-radius: 30px;"
            "   font-size: 20px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #e0e0e0;"
            "}"
        )
        self.setCursor(QCursor(Qt.PointingHandCursor))


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(500, 100, 400, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)

        top_space = QSpacerItem(1, 20)
        self.central_layout.addItem(top_space)

        self.result_display = QLineEdit(self)
        self.result_display.setFixedHeight(60)
        self.result_display.setAlignment(Qt.AlignRight)
        font = QFont()
        font.setPointSize(24)
        self.result_display.setFont(font)
        self.central_layout.addWidget(self.result_display)

        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['(', ')', '%', 'C']
        ]

        button_grid_layout = QGridLayout()
        for row_index, row in enumerate(button_grid):
            for col_index, text in enumerate(row):
                button = CalculatorButton(text, self)
                button.clicked.connect(self.on_button_click)
                button_grid_layout.addWidget(button, row_index, col_index)
        self.central_layout.addSpacing(30)
        self.central_layout.addLayout(button_grid_layout)

        bottom_space = QSpacerItem(1, 20)
        self.central_layout.addItem(bottom_space)

        self.result_display.returnPressed.connect(self.equals_button_click)

        self.result_display.textChanged.connect(self.restrict_input)

    def on_button_click(self):
        sender = self.sender()
        if sender:
            text = sender.text()
            if text == '=':
                self.equals_button_click()
            elif text == 'C':
                self.result_display.clear()
            else:
                current_text = self.result_display.text()
                self.result_display.setText(current_text + text)

    def equals_button_click(self):
        try:
            result = str(eval(self.result_display.text()))
            self.result_display.setText(result)
        except Exception as e:
            self.result_display.setText("Error")
            sleep(1)
            self.result_display.clear()

    def restrict_input(self):
        allowed_characters = r'0123456789\+\-\*/\(\)\.\%'
        current_text = self.result_display.text()
        filtered_text = ''.join(
            char for char in current_text if char in allowed_characters)
        self.result_display.setText(filtered_text)

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
