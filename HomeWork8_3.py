def type_logger(func):
    print(f'{func}: {type(func)}')
    return type_logger


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('*********************')
        func(*args, **kwargs)
        print('*********************')
    return wrapper


@func_decorator
@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5)
