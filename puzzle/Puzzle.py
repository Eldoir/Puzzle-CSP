from constraint import Problem
from typing import List
from rules.IRules import IRules
from domains.IDomain import IDomain

class Puzzle(object):
    def __init__(self, grid: List[List[int]], rules: List[IRules], domain_strategy: IDomain):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.variables = [[i * self.h + j for j in range(self.w)] for i in range(self.h)]
        self.rules = rules
        self.domain_strategy = domain_strategy
        self.__setup_done = False

    def setup_problem(self, problem: Problem):
        if self.__setup_done:
            raise AssertionError('Setup must be done only once.')
        self.__add_variables(problem)
        self.__add_constraints(problem)
    
    def __add_variables(self, problem: Problem):
        for i in range(self.h):
            for j in range(self.w):
                val = self.grid[i][j]
                variable = self.variables[i][j]
                if val != 0:
                    problem.addVariable(variable, domain=[val])
                else:
                    problem.addVariable(variable, domain=self.domain_strategy.get_domain(i, j))

    def __add_constraints(self, problem: Problem):
        for rule in self.rules:
            rule.add_constraints(problem, self.h, self.w, self.variables)