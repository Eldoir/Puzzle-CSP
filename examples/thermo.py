import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.rules.ThermoRules import ThermoRules
from puzzle.domains.RangeDomain import RangeDomain

# 0 means empty cell (no digit)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

thermos = [
    [(0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7)],
    [(1, 5), (2, 5), (3, 5), (3, 6)],
    [(2, 3), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)],
    [(5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (6, 1)],
    [(6, 5), (7, 5), (8, 5)],
    [(8, 6), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5)]
]

puzzle = Puzzle(grid, [SudokuRules(), ThermoRules(thermos)], RangeDomain(1, 10))
solve_puzzle(puzzle)