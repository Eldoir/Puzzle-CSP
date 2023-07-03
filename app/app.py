import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt
from SudokuGrid import SudokuGrid
from MainWindow import MainWindow
from ui.main_window import Ui_MainWindow
from ui.no_solution_dialog import Ui_Dialog
    
def main():
    def solve():
        grid.solve_command.execute()
        if grid.solve_command.result is False:
            popup = QDialog()
            popup.setWindowFlags(popup.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            Ui_Dialog().setupUi(popup)
            popup.exec_()

    app = QApplication(sys.argv)
    window = MainWindow()
    ui_window = Ui_MainWindow()
    ui_window.setupUi(window)
    grid = SudokuGrid()
    grid.setupUi(ui_window.gridLayout)

    # RELAY WINDOW <> GRID
    window.keyPressed.connect(grid.handleKeyPress)
    window.keyReleased.connect(grid.handleKeyRelease)

    # CONNECT BUTTONS
    ui_window.button_0.pressed.connect(lambda: grid.set_cell_value_command.execute(0))
    ui_window.button_1.pressed.connect(lambda: grid.set_cell_value_command.execute(1))
    ui_window.button_2.pressed.connect(lambda: grid.set_cell_value_command.execute(2))
    ui_window.button_3.pressed.connect(lambda: grid.set_cell_value_command.execute(3))
    ui_window.button_4.pressed.connect(lambda: grid.set_cell_value_command.execute(4))
    ui_window.button_5.pressed.connect(lambda: grid.set_cell_value_command.execute(5))
    ui_window.button_6.pressed.connect(lambda: grid.set_cell_value_command.execute(6))
    ui_window.button_7.pressed.connect(lambda: grid.set_cell_value_command.execute(7))
    ui_window.button_8.pressed.connect(lambda: grid.set_cell_value_command.execute(8))
    ui_window.button_9.pressed.connect(lambda: grid.set_cell_value_command.execute(9))
    ui_window.button_delete.pressed.connect(lambda: grid.delete_selected_cells_value_command.execute())

    ui_window.button_validate.pressed.connect(solve)

    window.setFocusPolicy(Qt.FocusPolicy.StrongFocus) # window accepts arrow keys
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()