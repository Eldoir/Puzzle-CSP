import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QVBoxLayout, QGridLayout, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Puzzle-CSP")

        self.grid = SudokuGrid()
        self.setCentralWidget(self.grid)

        # Center window on screen
        screen_rect = QDesktopWidget().availableGeometry()
        self.move((screen_rect.width() - self.width()) // 2, (screen_rect.height() - self.height()) // 2)

class Cell(QLabel):
    font: QFont = None
    defaultStyle: str = "background-color: white; border: 1px solid black;"
    selectedStyle: str = "background-color: blue; border: 1px solid black;"

    def __init__(self):
        super().__init__()
        if self.font is None:
            self.font = QFont()
            self.font.setPointSize(20)
        self.setFont(self.font)
        self.setFixedSize(40, 40)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(self.defaultStyle)

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        self.selected_cells = set()
        self.is_ctrl_pressed = False
        
        self.cells = []
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell()
                cell.mousePressEvent = lambda event, row=row, col=col: self.cell_clicked(event, row, col)
                row_cells.append(cell)
                grid_layout.addWidget(cell, row, col)
            self.cells.append(row_cells)
        
        layout.addLayout(grid_layout)
        
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_button_clicked)
        layout.addWidget(solve_button)
        
        self.setLayout(layout)
    
    def cell_clicked(self, event, row, col):
        cell = self.cells[row][col]
        if self.is_ctrl_pressed: # add cell to current selection
            self.update_selected_cells(self.selected_cells.copy() | {cell}, removed_cells=[])
        else: # set cell as current selection
            self.update_selected_cells([cell], self.selected_cells.copy())
    
    def keyPressEvent(self, event):
        key = event.key()
        if key >= 49 and key <= 57: #numpad 1-9
            self.set_selected_cells_text(str(key - 48))
        elif key == 16777219: # backspace
            self.set_selected_cells_text("")
        elif key == 16777249: # ctrl (left/right)
            self.is_ctrl_pressed = True
        print(f"Key pressed: {key}")

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == 16777249: # ctrl (left/right)
            self.is_ctrl_pressed = False

    def set_selected_cells_text(self, text: str):
        for cell in self.selected_cells:
            cell.setText(text)

    def update_selected_cells(self, added_cells, removed_cells):
        for cell in removed_cells:
            cell.setStyleSheet(Cell.defaultStyle)
            self.selected_cells.remove(cell)
        for cell in added_cells:
            cell.setStyleSheet(Cell.selectedStyle)
            self.selected_cells.add(cell)

    def solve_button_clicked(self):
        popup = QMessageBox(QMessageBox.Information, 'Popup', 'Solving...', QMessageBox.Ok)
        popup.exec_()
    
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()