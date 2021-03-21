import sys


def odd_num(num):
    for el in (el for el in range(1, num, 2)):
        yield el
# генератор нечетных чисел, используя yield


x = odd_num(15)
print(type(x), sys.getsizeof(x))
for i in odd_num(15):
    print(next(x))
