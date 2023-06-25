from puzzle.Puzzle import Puzzle
from constraint import Problem

#TODO: fix warning message not displayed before second iteration is done computing

def solve_puzzle(puzzle: Puzzle):
    problem = Problem()
    puzzle.setup_problem(problem)

    iter = problem.getSolutionIter()
    solution = None
    try:
        solution = next(iter)
    except StopIteration:
        print("No solution")
        return

    print_sudoku(solution, puzzle.h, puzzle.w)
    try:
        solution = next(iter)
        print("WARNING: non-unique solution, other example:")
        print_sudoku(solution, puzzle.h, puzzle.w)
    except StopIteration:
        print("This solution is unique!")

def print_sudoku(solution, h, w):
    for i in range(h):
        for j in range(w):
            print(solution[i * h + j], end=' ')
        print("")