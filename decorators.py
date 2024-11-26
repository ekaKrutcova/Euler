from time import time
from functools import wraps

def time_execution(func):
    '''
    Log a time execution of the provided function `func` to the console

    arguments:
    func -- the function to run
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func_output = func(*args, **kwargs)
        end = time()
        time_execution = end - start
        print(f'{func.__name__} with args: {args}, kwargs: {kwargs} execution took {time_execution:.5f} sec')
        return func_output
    return wrapper