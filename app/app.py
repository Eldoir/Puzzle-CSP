import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from SudokuGrid import SudokuGrid
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow(title="Puzzle-CSP")
    grid = SudokuGrid()
    window.setCentralWidget(grid)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()