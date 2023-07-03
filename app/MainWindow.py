from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QKeyEvent

class MainWindow(QMainWindow):
    keyPressed = pyqtSignal(QKeyEvent)
    keyReleased = pyqtSignal(QKeyEvent)

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.keyPressed.emit(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        self.keyReleased.emit(event)