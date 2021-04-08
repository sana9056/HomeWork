def type_logger(func):

    def log_wrapper(*args, **kwargs):
        print('**********************')
        print(f'{func(*args, **kwargs)}: {type(func(*args, **kwargs))}')
        print('**********************')
    return log_wrapper

@type_logger
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
