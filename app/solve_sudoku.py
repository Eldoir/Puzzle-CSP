import __init__
from puzzle.solve import solve_puzzle
from puzzle.Puzzle import Puzzle
from puzzle.rules.SudokuRules import SudokuRules
from puzzle.domains.RangeDomain import RangeDomain
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    puzzle = Puzzle(grid, [SudokuRules()], RangeDomain(1, 10))
    return solve_puzzle(puzzle)
