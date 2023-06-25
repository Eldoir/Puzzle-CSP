from puzzle.Puzzle import Puzzle
from puzzle.domains.IDomain import RangeDomain
from puzzle.solve import solve_puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.rules.KillerRules import KillerRules
from puzzle.rules.SqrRules import SqrRules

# 0 means empty cell (no digit)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 4],
]

killer_groups = [
    (13, [(1, 8), (2, 8)]),
    (13, [(2, 6), (2, 7)]),
    (13, [(3, 6), (4, 6)]),
    (13, [(4, 0), (4, 1)]),
    (13, [(4, 3), (5, 3)]),
    (13, [(4, 4), (4, 5)]),
    (13, [(6, 3), (7, 3)]),
]

sqr_pairs = [
    ((2, 2), (3, 2)),
    ((3, 2), (3, 3)),
    ((3, 4), (3, 5)),
]

puzzle = Puzzle(grid, [
    SudokuRules(),
    KillerRules(killer_groups),
    SqrRules(sqr_pairs, full=True)
], RangeDomain(1, 10))

solve_puzzle(puzzle)