def val_checker(f):
   def _logger(func):
       def wrapper(*args):
           if f(*args) == True:
                   print(func(*args))
           else:
               num = args
               print(f'ValueError: wrong val: {args[0]}')
           return func
       return wrapper
   return _logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
