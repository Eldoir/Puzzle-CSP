import sys
from PyQt5.QtWidgets import QApplication
from MyWindow import MyWindow
from SudokuGrid import SudokuGrid
    
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    grid = SudokuGrid()
    window.setCentralWidget(grid)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()