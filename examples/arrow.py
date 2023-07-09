import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.rules.ArrowRules import ArrowRules, Arrow
from puzzle.domains.RangeDomain import RangeDomain

# 0 means empty cell (no digit)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [1, 0, 6, 0, 0, 0, 9, 0, 5],
    [0, 0, 2, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

arrows = [
    Arrow((0, 1), [(1, 0), (2, 1), (3, 1)]),
    Arrow((0, 2), [(1, 3), (2, 2), (3, 2)]),
    Arrow((0, 2), [(0, 3), (1, 4)]),
    Arrow((0, 6), [(0, 5), (1, 4)]),
    Arrow((0, 6), [(1, 5), (2, 6), (3, 6)]),
    Arrow((0, 7), [(1, 8), (2, 7), (3, 7)]),
    Arrow((3, 4), [(3, 3), (4, 3)]),
    Arrow((3, 4), [(3, 5), (4, 5)]),
    Arrow((6, 5), [(5, 4), (6, 3)]),
    Arrow((6, 7), [(7, 7), (8, 7)]),
    Arrow((7, 3), [(6, 4), (7, 5)]),
    Arrow((8, 1), [(7, 1), (6, 1)]),
    Arrow((8, 5), [(7, 4), (8, 3)])
]

puzzle = Puzzle(grid, [SudokuRules(), ArrowRules(arrows)], RangeDomain(1, 10))
solve_puzzle(puzzle)