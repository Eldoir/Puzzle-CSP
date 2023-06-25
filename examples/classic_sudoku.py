import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.domains.RangeDomain import RangeDomain

# 0 means empty cell (no digit)
grid = [
    [0, 2, 0, 5, 0, 1, 0, 9, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 6],
    [0, 3, 0, 0, 6, 0, 0, 7, 0],
    [0, 0, 1, 0, 0, 0, 6, 0, 0],
    [5, 4, 0, 0, 0, 0, 0, 1, 9],
    [0, 0, 2, 0, 0, 0, 7, 0, 0],
    [0, 9, 0 ,0, 3, 0, 0, 8, 0],
    [2, 0, 0, 8, 0, 4, 0, 0, 7],
    [0, 1, 0, 9, 0, 7, 0, 6, 0]
]

puzzle = Puzzle(grid, [SudokuRules()], RangeDomain(1, 10))
solve_puzzle(puzzle)