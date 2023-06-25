import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.TectonicRules import TectonicRules
from puzzle.domains.TectonicDomain import TectonicDomain

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 4, 0],
    [0, 0, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 0, 0, 0],
    [0, 0, 3, 0, 2, 0, 0],
    [1, 0, 0, 0, 0, 4, 0],
]

tectonic_groups = [
    [(0, 0)],
    [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)],
    [(0, 3), (0, 4), (0, 5), (1, 4), (1, 5)],
    [(0, 6)],
    [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0)],
    [(1, 6), (2, 6), (3, 6)],
    [(2, 2)],
    [(2, 4), (2, 5), (3, 4), (3, 5), (4, 5)],
    [(3, 1), (3, 2), (4, 1), (4, 2), (5, 2)],
    [(3, 3), (4, 3), (4, 4), (5, 3), (5, 4)],
    [(4, 0), (5, 0), (5, 1), (6, 1), (6, 2)],
    [(4, 6)],
    [(5, 5), (5, 6), (6, 5), (6, 6), (7, 6)],
    [(6, 0), (7, 0), (7, 1), (8, 0), (8, 1)],
    [(6, 3), (7, 2), (7, 3), (8, 2), (8, 3)],
    [(6, 4), (7, 4), (7, 5), (8, 4), (8, 5)],
    [(8, 6)]
]

puzzle = Puzzle(grid, [TectonicRules(tectonic_groups)], TectonicDomain(tectonic_groups))
solve_puzzle(puzzle)