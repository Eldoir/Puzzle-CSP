from IDomain import IDomain
from typing import Any

class RangeDomain(IDomain):
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def get_domain(self, x_var: int, y_var: int) -> Any:
        return range(self.min, self.max)