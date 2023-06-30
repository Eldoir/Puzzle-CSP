from constraint import Problem
from typing import List, Tuple
from IRules import IRules

from enum import Enum
class KropkiMode(Enum):
    WHITE = 1
    BLACK = 2

class KropkiRules(IRules):
    def __init__(self, pairs: List[Tuple[Tuple[int, int], Tuple[int, int], KropkiMode]], full: bool = False):
        self.pairs = pairs
        self.full = full

    def add_constraints(self, problem: Problem, h: int, w: int, variables: List[List[int]]):
        for (x1, y1), (x2, y2), mode in self.pairs:
            func = self.white_dot if mode == KropkiMode.WHITE else self.black_dot
            problem.addConstraint(func, [variables[x1][y1], variables[x2][y2]])
        
        if self.full:
            for i in range(h):
                for j in range(w):
                    if i > 0 and not self.pair_exists((i, j), (i - 1, j)):
                        problem.addConstraint(self.not_white_nor_black, [variables[i][j], variables[i - 1][j]]) # top
                    if i < h - 1 and not self.pair_exists((i, j), (i + 1, j)):
                        problem.addConstraint(self.not_white_nor_black, [variables[i][j], variables[i + 1][j]]) # bottom
                    if j > 0 and not self.pair_exists((i, j), (i, j - 1)):
                        problem.addConstraint(self.not_white_nor_black, [variables[i][j], variables[i][j - 1]]) # left
                    if j < w - 1 and not self.pair_exists((i, j), (i, j + 1)):
                        problem.addConstraint(self.not_white_nor_black, [variables[i][j], variables[i][j + 1]]) # right

    def white_dot(self, a, b) -> bool:
        return abs(a - b) == 1
    
    def black_dot(self, a, b) -> bool:
        return a == 2 * b or b == 2 * a
    
    def not_white_nor_black(self, a, b) -> bool:
        return not self.white_dot(a, b) and not self.black_dot(a, b)
    
    def pair_exists(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
        for (x1, y1), (x2, y2), _ in self.pairs:
            if x1 == p1[0] and y1 == p1[1] and x2 == p2[0] and y2 == p2[1] or\
               x1 == p2[0] and y1 == p2[1] and x2 == p1[0] and y2 == p1[1]: 
                return True
        return False