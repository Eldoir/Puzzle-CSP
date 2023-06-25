from constraint import Problem, AllDifferentConstraint
from typing import List
from IRules import IRules

class SudokuRules(IRules):
    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        # add constraint on rows
        for i in range(h):
            problem.addConstraint(AllDifferentConstraint(), [variables[i][j] for j in range(w)])

        # add constraint on columns
        for j in range(w):
            problem.addConstraint(AllDifferentConstraint(), [variables[i][j] for i in range(h)])
        
        # add constraint on blocks
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                problem.addConstraint(AllDifferentConstraint(), [(variables[i + ii][j + jj]) for ii in range(3) for jj in range(3)])