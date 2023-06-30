from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Cell(QLabel):
    font: QFont = None
    defaultStyle: str = "background-color: white; border: 1px solid black;"
    selectedStyle: str = "background-color: blue; border: 1px solid black;"
    value: int = 0

    def __init__(self):
        super().__init__()
        if self.font is None:
            self.font = QFont()
            self.font.setPointSize(20)
        self.setFont(self.font)
        self.setFixedSize(40, 40)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(self.defaultStyle)

    def set_value(self, value):
        self.value = value
        self.setText(str(value))

    def delete_value(self):
        self.value = 0
        self.setText("")