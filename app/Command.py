from typing import TypeVar, Generic, Callable

class ICommand:
    def execute(self, *args) -> None:
        raise NotImplementedError()

class Command(ICommand):
    def __init__(self, func: Callable):
        self.__func = func

    def execute(self, *args) -> None:
        self.__func(*args)

T = TypeVar('T')  # Type variable for generic type
class CommandWithResult(ICommand, Generic[T]):
    def __init__(self, func: Callable):
        self.__func = func
    
    def execute(self, *args) -> None:
        self.result = self.__func(*args)

