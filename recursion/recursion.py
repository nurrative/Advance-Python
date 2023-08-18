# Рекурсия - функция, которая вызывает сам себя

# Факториал

# def factorial(num):
#     return_value = 1;
#     for i in range(2, num + 1):
#         return_value *= i
#     return return_value
#
# print(factorial(5))

# def factorial(num):
#     return 1 if num<=1 else num * factorial(num-1)
#
# if __name__ == '__main__':
#     print(factorial(5))

from functools import reduce

def fact_with_reduce(num):
    return reduce(lambda x,y:x*y, range(1,num+1) or [1])

print(fact_with_reduce(5))

from math import factorial

print(factorial(5))