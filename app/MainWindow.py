from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self, title: str):
        super().__init__()

        self.setWindowTitle(title)
        self.center_on_screen()    

    def center_on_screen(self):
        screen_rect = QDesktopWidget().availableGeometry()
        self.move((screen_rect.width() - self.width()) / 2, (screen_rect.height() - self.height()) / 2)