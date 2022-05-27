from typing import Callable

def copy_doc(copy_func: Callable) -> Callable:
    """Use Example: copy_doc(self.copy_func)(self.func) or used as deco"""
    def wrapper(func: Callable) -> Callable:
        func.__doc__ = copy_func.__doc__
        return func
    return wrapper

class Test:
    def foo(self) -> None:
        """Woa"""
        ...
    
    @copy_doc(foo)
    def this(self) -> None:
        ...
    

print(Test().this.__doc__)

# # Outputs:
# > Woa