from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Puzzle-CSP")

        # Center window on screen
        screen_rect = QDesktopWidget().availableGeometry()
        self.move((screen_rect.width() - self.width()) / 2, (screen_rect.height() - self.height()) / 2)