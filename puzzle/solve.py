from puzzle.Puzzle import Puzzle
from constraint import Problem
from typing import List

#TODO: fix warning message not displayed before second iteration is done computing

def solve_puzzle(puzzle: Puzzle) -> List[List[int]]:
    problem = Problem()
    puzzle.setup_problem(problem)

    iter = problem.getSolutionIter()
    solution = None
    try:
        solution = next(iter)
    except StopIteration:
        print("No solution")
        return None

    sudoku = get_sudoku(solution, puzzle.h, puzzle.w)
    print_sudoku(sudoku)
    try:
        solution = next(iter)
        print("WARNING: non-unique solution, other example:")
        print_sudoku(get_sudoku(solution, puzzle.h, puzzle.w))
    except StopIteration:
        print("This solution is unique!")

    return sudoku

def get_sudoku(solution, h, w) -> List[List[int]]:
    sudoku = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(solution[i * h + j])
        sudoku.append(row)
    return sudoku

def print_sudoku(sudoku):
    i = 0
    for row in sudoku:
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        j = 0
        for cell in row:
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(cell, end=' ')
            j += 1
        i += 1 
        print()
