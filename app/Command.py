from typing import NoReturn, TypeVar, Generic, Callable

class ICommand:
    def execute(self, *args) -> NoReturn:
        raise NotImplementedError()

class Command(ICommand):
    def __init__(self, func: Callable):
        self.__func = func

    def execute(self, *args) -> NoReturn:
        self.__func(*args)

T = TypeVar('T')  # Type variable for generic type
class CommandWithResult(ICommand, Generic[T]):
    def __init__(self, func: Callable):
        self.__func = func
    
    def execute(self, *args) -> NoReturn:
        self.result = self.__func(*args)

