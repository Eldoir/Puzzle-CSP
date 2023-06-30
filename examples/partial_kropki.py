import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.rules.KropkiRules import KropkiRules, KropkiMode
from puzzle.domains.RangeDomain import RangeDomain

# 0 means empty cell (no digit)
grid = [
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 2, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 6],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [3, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

kropki_pairs = [
    ((0, 2), (1, 2), KropkiMode.WHITE), ((1, 6), (1, 7), KropkiMode.WHITE),
    ((2, 3), (3, 3), KropkiMode.WHITE), ((2, 7), (3, 6), KropkiMode.WHITE),
    ((3, 5), (4, 5), KropkiMode.WHITE), ((4, 1), (5, 1), KropkiMode.WHITE),
    ((4, 7), (4, 8), KropkiMode.WHITE), ((5, 6), (6, 6), KropkiMode.WHITE),
    ((6, 1), (6, 2), KropkiMode.WHITE), ((7, 3), (8, 3), KropkiMode.WHITE)
]

puzzle = Puzzle(grid, [SudokuRules(), KropkiRules(kropki_pairs)], RangeDomain(1, 10))
solve_puzzle(puzzle)