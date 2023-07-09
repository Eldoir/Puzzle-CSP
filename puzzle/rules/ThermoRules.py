from constraint import Problem
from typing import List, Tuple
from IRules import IRules

class ThermoRules(IRules):
    def __init__(self, thermos: List[List[Tuple[int, int]]]):
        self.thermos = thermos

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for thermo in self.thermos:
            related_variables = [variables[x][y] for x,y in thermo]
            problem.addConstraint(self.ascending_constraint, related_variables)

    def ascending_constraint(self, *args):
        return all(args[i] < args[i+1] for i in range(len(args)-1))
