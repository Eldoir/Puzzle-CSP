from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtCore import Qt, QRect, pyqtSlot
from Cell import Cell
from collections.abc import Iterable
from Keyboard import Key
from typing import Tuple
from solve_sudoku import solve
from Command import Command, CommandWithResult

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        self.selected_cells: set[Cell] = set()
        self.cells: List[List[Cell]] = []
        self.last_selected_cell_pos: Tuple[int, int] = None

        self.is_ctrl_pressed = False
        self.is_left_mouse_pressed = False

        # COMMANDS
        self.set_cell_value_command = Command(self.set_selected_cells_value)
        self.delete_selected_cells_value_command = Command(self.delete_selected_cells_value)
        self.solve_command = CommandWithResult[bool](self.solve)
    
    def setupUi(self, grid_layout: QGridLayout):
        grid_layout.setSpacing(0)

        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell()
                cell.mousePressEvent = lambda event, cell=cell: self.cell_clicked(event, cell)
                row_cells.append(cell)
                grid_layout.addWidget(cell, row, col)
            self.cells.append(row_cells)
    
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

    @pyqtSlot(QMouseEvent)
    def handleMousePress(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.is_left_mouse_pressed = True

    @pyqtSlot(QMouseEvent)
    def handleMouseRelease(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.is_left_mouse_pressed = False
    
    @pyqtSlot(QKeyEvent)
    def handleKeyPress(self, event: QKeyEvent):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key == Key.BACKSPACE or key == Key.DELETE:
            self.delete_selected_cells_value()
        elif key == Key.CTRL_LEFT_RIGHT:
            self.is_ctrl_pressed = True
        elif key == Key.Z or key == Key.ARROW_UP:
            if self.last_selected_cell_pos is not None:
                next_cell = self.get_cell_with_dir(self.last_selected_cell_pos, (-1, 0))
                self.set_cell_as_current_selection(next_cell)
        elif key == Key.Q or key == Key.ARROW_LEFT:
            if self.last_selected_cell_pos is not None:
                next_cell = self.get_cell_with_dir(self.last_selected_cell_pos, (0, -1))
                self.set_cell_as_current_selection(next_cell)
        elif key == Key.S or key == Key.ARROW_DOWN:
            if self.last_selected_cell_pos is not None:
                next_cell = self.get_cell_with_dir(self.last_selected_cell_pos, (1, 0))
                self.set_cell_as_current_selection(next_cell)
        elif key == Key.D or key == Key.ARROW_RIGHT:
            if self.last_selected_cell_pos is not None:
                next_cell = self.get_cell_with_dir(self.last_selected_cell_pos, (0, 1))
                self.set_cell_as_current_selection(next_cell)

    @pyqtSlot(QKeyEvent)
    def handleKeyRelease(self, event: QKeyEvent):
        key = event.key()
        if key == Key.CTRL_LEFT_RIGHT:
            self.is_ctrl_pressed = False

    def get_cell(self, row: int, col: int) -> Cell:
        return self.cells[row][col]
    
    def get_cell_with_dir(self, cell_pos: Tuple[int, int], dir: Tuple[int, int]) -> Cell:
        row = cell_pos[0] + dir[0]
        if row == -1:
            row = len(self.cells) - 1
        elif row >= len(self.cells):
            row = 0
        col = cell_pos[1] + dir[1]
        if col == -1:
            col = len(self.cells[0]) - 1
        elif col >= len(self.cells[0]):
            col = 0
        return self.get_cell(row, col)

    def set_selected_cells_value(self, value: int):
        for cell in self.selected_cells:
            cell.set_value(value)

    def delete_selected_cells_value(self):
        for cell in self.selected_cells:
            cell.delete_value()

    def add_to_selected_cells(self, cell: Cell):
        self.update_selected_cells(added_cells=[cell], removed_cells=[])
        self.set_last_selected_cell(cell)

    def remove_from_selected_cells(self, cell: Cell):
        self.update_selected_cells(added_cells=[], removed_cells=[cell])

    def set_cell_as_current_selection(self, cell: Cell):
        self.update_selected_cells(added_cells=[cell], removed_cells=self.selected_cells.copy())
        self.set_last_selected_cell(cell)

    def update_selected_cells(self, added_cells: Iterable[Cell], removed_cells: Iterable[Cell]):
        for cell in removed_cells:
            cell.set_selected(False)
            self.selected_cells.remove(cell)
        for cell in added_cells:
            cell.set_selected(True)
            self.selected_cells.add(cell)
        
        if len(self.selected_cells) == 0:
            self.set_last_selected_cell(None)
        
    def set_last_selected_cell(self, cell: Cell):
        if cell is None:
            self.last_selected_cell_pos = None

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.get_cell(row, col) == cell:
                    self.last_selected_cell_pos = (row, col)

    def get_grid_values(self) -> List[List[int]]:
        return [[cell.value for cell in row] for row in self.cells]
    
    def apply_values(self, grid: List[List[int]]):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.cells[row][col].set_value(grid[row][col])

    """
    Returns whether a solution was found.
    """
    def solve(self) -> bool:
        new_grid = solve(self.get_grid_values())
        has_solution = new_grid is not None
        if has_solution:
            self.apply_values(new_grid)
        return has_solution