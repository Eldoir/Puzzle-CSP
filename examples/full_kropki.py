import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.rules.KropkiRules import KropkiRules, KropkiMode
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

kropki_pairs = [
    ((0, 0), (0, 1), KropkiMode.WHITE), ((0, 5), (0, 6), KropkiMode.BLACK),
    ((1, 0), (2, 0), KropkiMode.WHITE), ((1, 3), (1, 4), KropkiMode.WHITE),
    ((2, 0), (3, 0), KropkiMode.BLACK), ((2, 1), (3, 1), KropkiMode.BLACK),
    ((2, 3), (3, 3), KropkiMode.WHITE), ((2, 5), (3, 5), KropkiMode.BLACK),
    ((3, 0), (3, 1), KropkiMode.BLACK), ((3, 1), (3, 2), KropkiMode.WHITE),
    ((3, 7), (3, 8), KropkiMode.WHITE), ((4, 1), (5, 1), KropkiMode.WHITE),
    ((4, 2), (5, 2), KropkiMode.BLACK), ((4, 6), (5, 6), KropkiMode.WHITE),
    ((4, 6), (4, 7), KropkiMode.BLACK), ((4, 7), (4, 8), KropkiMode.WHITE),
    ((5, 2), (5, 3), KropkiMode.WHITE), ((5, 3), (5, 4), KropkiMode.BLACK),
    ((6, 0), (7, 0), KropkiMode.WHITE), ((6, 1), (7, 1), KropkiMode.WHITE),
    ((6, 4), (7, 4), KropkiMode.WHITE), ((6, 5), (6, 6), KropkiMode.WHITE),
    ((7, 5), (7, 6), KropkiMode.WHITE), ((7, 6), (8, 6), KropkiMode.WHITE),
    ((7, 7), (7, 8), KropkiMode.BLACK), ((8, 7), (8, 8), KropkiMode.WHITE)
]

puzzle = Puzzle(grid, [SudokuRules(), KropkiRules(kropki_pairs, full=True)], RangeDomain(1, 10))
solve_puzzle(puzzle)