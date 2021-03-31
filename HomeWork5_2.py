import sys


def odd_num(num):
    return (el for el in range(1, num, 2))
# генератор нечетных чисел, не используя yield


x = odd_num(15)
print(type(x), sys.getsizeof(x))
for i in odd_num(15):
    print(next(x))
