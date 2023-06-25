from constraint import Problem
from typing import List, Tuple
from IRules import IRules

class SqrRules(IRules):
    def __init__(self, pairs: List[Tuple[Tuple[int]]], full: bool = False):
        self.pairs = pairs
        self.full = full

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for (i1, j1), (i2, j2) in self.pairs:
            problem.addConstraint(self.is_sqr, [variables[i1][j1], variables[i2][j2]])

        if self.full:
            for i in range(h):
                for j in range(w):
                    if i > 0:
                        problem.addConstraint(self.not_sqr, [variables[i][j], variables[i - 1][j]]) # top
                    if i < h - 1:
                        problem.addConstraint(self.not_sqr, [variables[i][j], variables[i + 1][j]]) # bottom
                    if j > 0:
                        problem.addConstraint(self.not_sqr, [variables[i][j], variables[i][j - 1]]) # left
                    if j < w - 1:
                        problem.addConstraint(self.not_sqr, [variables[i][j], variables[i][j + 1]]) # right

    def is_sqr(self, a, b) -> bool:
        return a == b * b or b == a * a
    
    def not_sqr(self, a, b) -> bool:
        return not self.is_sqr(a, b)