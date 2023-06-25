from constraint import Problem, AllDifferentConstraint
from typing import List, Tuple
from IRules import IRules

class TectonicRules(IRules):
    def __init__(self, groups: List[List[Tuple[int, int]]]):
        is_valid, error = self.are_groups_valid(groups)
        if not is_valid:
            raise AssertionError(error)
        self.groups = groups

    def are_groups_valid(self, groups) -> Tuple[bool, str]:
        concerned_cells = []
        for cells in groups:
            for x, y in cells:
                for c_x, c_y in concerned_cells:
                    if c_x == x and y == c_y:
                        return (False, f'ERROR : Cell ({x}, {y}) is implied in multiple groups')
                concerned_cells.append((x, y))
        return (True, '')

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for cells in self.groups:
            if len(cells) > 0:
                related_variables = [variables[x][y] for x,y in cells]
                problem.addConstraint(AllDifferentConstraint(), related_variables)

        for i in range(h):
            for j in range(w):
                if i > 0:
                    problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i - 1][j]]) # top
                    if j > 0:
                        problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i - 1][j - 1]]) # top left
                    if j < w - 1:
                        problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i - 1][j + 1]]) # top right
                if i < h - 1:
                    problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i + 1][j]]) # bottom
                    if j > 0:
                        problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i + 1][j - 1]]) # bottom left
                    if j < w - 1:
                        problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i + 1][j + 1]]) # bottom right
                if j > 0:
                    problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i][j - 1]]) # left
                if j < w - 1:
                    problem.addConstraint(AllDifferentConstraint(), [variables[i][j], variables[i][j + 1]]) # right