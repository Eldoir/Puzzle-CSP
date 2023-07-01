from typing import List
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtCore import Qt, QRect
from Cell import Cell
from collections.abc import Iterable
from Keyboard import Key

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        self.selected_cells: set[Cell] = set()
        self.cells: List[List[Cell]] = []

        self.is_ctrl_pressed = False
        self.is_left_mouse_pressed = False

        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)
        
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell()
                cell.mousePressEvent = lambda event, cell=cell: self.cell_clicked(event, cell)
                row_cells.append(cell)
                grid_layout.addWidget(cell, row, col)
            self.cells.append(row_cells)
        
        layout.addLayout(grid_layout)
        
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_button_clicked)
        layout.addWidget(solve_button)
        
        self.setLayout(layout)
    
    def cell_clicked(self, event: QMouseEvent, cell: Cell):
        if event.button() == Qt.LeftButton:
            if self.is_ctrl_pressed:
                if cell.is_selected:
                    self.remove_from_selected_cells(cell)
                else:
                    self.add_to_selected_cells(cell)
            else:
                if self.selected_cells == {cell}:
                    self.remove_from_selected_cells(cell)
                else:
                    self.set_cell_as_current_selection(cell)
            
            self.is_left_mouse_pressed = True

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_left_mouse_pressed:
            pos = event.pos()
            for row in self.cells:
                for cell in row:
                    if not cell.is_selected:
                        if QRect(cell.pos().x(), cell.pos().y(), cell.rect().width(), cell.rect().height()).contains(pos):
                            self.add_to_selected_cells(cell)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.is_left_mouse_pressed = True

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.is_left_mouse_pressed = False
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key >= Key.NUMPAD_1 and key <= Key.NUMPAD_9:
            self.set_selected_cells_value(key - Key.NUMPAD_0)
        elif key == Key.BACKSPACE or key == Key.DELETE:
            self.delete_selected_cells_value()
        elif key == Key.CTRL_LEFT_RIGHT:
            self.is_ctrl_pressed = True
        print(f"Key pressed: {key}")

    def keyReleaseEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Key.CTRL_LEFT_RIGHT:
            self.is_ctrl_pressed = False

    def set_selected_cells_value(self, value: int):
        for cell in self.selected_cells:
            cell.set_value(value)

    def delete_selected_cells_value(self):
        for cell in self.selected_cells:
            cell.delete_value()

    def add_to_selected_cells(self, cell: Cell):
        self.update_selected_cells(added_cells=[cell], removed_cells=[])

    def remove_from_selected_cells(self, cell: Cell):
        self.update_selected_cells(added_cells=[], removed_cells=[cell])

    def set_cell_as_current_selection(self, cell: Cell):
        self.update_selected_cells(added_cells=[cell], removed_cells=self.selected_cells.copy())

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