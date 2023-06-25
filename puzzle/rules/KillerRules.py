from constraint import Problem, AllDifferentConstraint, ExactSumConstraint
from typing import List, Tuple
from IRules import IRules

class KillerRules(IRules):
    def __init__(self, groups: List[Tuple[int, List[Tuple[int, int]]]]):
        is_valid, error = self.are_groups_valid(groups)
        if not is_valid:
            raise AssertionError(error)
        self.groups = groups

    def are_groups_valid(self, groups) -> Tuple[bool, str]:
        concerned_cells = []
        for sum, cells in groups:
            for x, y in cells:
                for c_x, c_y in concerned_cells:
                    if c_x == x and y == c_y:
                        return (False, f'ERROR : Cell ({x}, {y}) is implied in multiple groups')
                concerned_cells.append((x, y))
        return (True, '')

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for sum, cells in self.groups:
            if len(cells) > 0:
                related_variables = [variables[x][y] for x,y in cells]
                problem.addConstraint(AllDifferentConstraint(), related_variables)
                if sum != 0:
                    problem.addConstraint(ExactSumConstraint(sum), related_variables)