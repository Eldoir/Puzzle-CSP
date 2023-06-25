from typing import Any

class IDomain(object):
    def get_domain(self, x_var: int, y_var: int) -> Any:
        raise NotImplementedError()