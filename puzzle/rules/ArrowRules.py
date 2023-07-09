from constraint import Problem
from typing import List, Tuple
from IRules import IRules

class Arrow:
    def __init__(self, base: Tuple[int, int], shaft: List[Tuple[int, int]]):
        self.base = base
        self.shaft = shaft

class ArrowRules(IRules):
    def __init__(self, arrows: List[Arrow]):
        self.arrows = arrows

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for arrow in self.arrows:
            base_variable = variables[arrow.base[0]][arrow.base[1]]
            shaft_variables = [variables[x][y] for x,y in arrow.shaft]
            problem.addConstraint(self.sum_constraint, [base_variable, *shaft_variables])

    def sum_constraint(self, base, *args):
        return base == sum(args)
