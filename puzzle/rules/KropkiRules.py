from constraint import Problem
from typing import List, Tuple
from IRules import IRules

# TODO: add black dots
# TODO: add full or partial constraint

class KropkiRules(IRules):
    def __init__(self, pairs: List[Tuple[Tuple[int, int]]]):
        self.pairs = pairs

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for (x1, y1), (x2, y2) in self.pairs:
            problem.addConstraint(self.white_dot, [variables[x1][y1], variables[x2][y2]])

    def white_dot(self, a, b):
        return abs(a - b) == 1