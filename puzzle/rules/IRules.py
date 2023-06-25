from constraint import Problem
from typing import List

class IRules(object):
    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        raise NotImplementedError()