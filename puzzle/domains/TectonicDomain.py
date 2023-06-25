from IDomain import IDomain
from typing import Any, List, Tuple

class TectonicDomain(IDomain):
    def __init__(self, groups: List[List[Tuple[int, int]]]):
        self.groups = groups

    def get_domain(self, x_var: int, y_var: int) -> Any:
        for cells in self.groups:
            for x,y in cells:
                if x == x_var and y == y_var:
                    return range(1, len(cells) + 1)
        raise ValueError(f'Cell ({x_var}, {y_var}) is not any group.')