from typing import List
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QKeyEvent, QMouseEvent
from Cell import Cell
from collections.abc import Iterable

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        self.selected_cells: set[Cell] = set()
        self.is_ctrl_pressed = False
        self.cells: List[List[Cell]] = []

        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)
        
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
    
    def cell_clicked(self, event: QMouseEvent, row: int, col: int):
        cell = self.cells[row][col]
        if self.is_ctrl_pressed: # add cell to current selection
            self.add_to_selected_cells(cell)
        else: # set cell as current selection
            self.set_cell_as_current_selection(cell)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key >= 49 and key <= 57: #numpad 1-9
            self.set_selected_cells_value(key - 48)
        elif key == 16777219 or key == 16777223: # backspace or delete
            self.delete_selected_cells_value()
        elif key == 16777249: # ctrl (left/right)
            self.is_ctrl_pressed = True
        print(f"Key pressed: {key}")

    def keyReleaseEvent(self, event: QKeyEvent):
        key = event.key()
        if key == 16777249: # ctrl (left/right)
            self.is_ctrl_pressed = False

    def set_selected_cells_value(self, value: int):
        for cell in self.selected_cells:
            cell.set_value(value)

    def delete_selected_cells_value(self):
        for cell in self.selected_cells:
            cell.delete_value()

    def add_to_selected_cells(self, cell: Cell):
        self.update_selected_cells(self.selected_cells.copy() | {cell}, removed_cells=[])

    def set_cell_as_current_selection(self, cell: Cell):
        self.update_selected_cells([cell], self.selected_cells.copy())

    def update_selected_cells(self, added_cells: Iterable[Cell], removed_cells: Iterable[Cell]):
        for cell in removed_cells:
            cell.set_selected(False)
            self.selected_cells.remove(cell)
        for cell in added_cells:
            cell.set_selected(True)
            self.selected_cells.add(cell)

    def solve_button_clicked(self):
        popup = QMessageBox(QMessageBox.Information, 'Popup', 'Solving...', QMessageBox.Ok)
        popup.exec_()