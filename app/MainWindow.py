from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QKeyEvent, QMouseEvent

class MainWindow(QMainWindow):
    keyPressed = pyqtSignal(QKeyEvent)
    keyReleased = pyqtSignal(QKeyEvent)
    mousePressed = pyqtSignal(QMouseEvent)
    mouseReleased = pyqtSignal(QMouseEvent)

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.keyPressed.emit(event)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        self.keyReleased.emit(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mousePressed.emit(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouseReleased.emit(event)