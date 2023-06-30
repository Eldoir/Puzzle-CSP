from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Cell(QWidget):
    font: QFont = None
    defaultStyle: str = "background-color: white; border: 1px solid black;"
    selectedStyle: str = "background-color: blue; border: 1px solid black;"
    value: int = 0

    def __init__(self):
        super().__init__()
        if self.font is None:
            self.font = QFont()
            self.font.setPointSize(20)
        
        self.label = QLabel()
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignCenter)

        self.setFixedSize(50, 50)
        self.setStyleSheet(self.defaultStyle)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_value(self, value: int):
        self.value = value
        self.label.setText(str(value))

    def delete_value(self):
        self.value = 0
        self.label.setText("")

    def set_selected(self, selected: bool):
        self.setStyleSheet(self.selectedStyle if selected else self.defaultStyle)