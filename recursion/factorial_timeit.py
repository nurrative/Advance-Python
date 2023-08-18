from timeit import timeit

### recursive

stmt = """def factorial(num):
             return 1 if num<=1 else num * factorial(num-1)
"""

print("Recursive:", timeit('factorial(5)', setup = stmt, number=1000000))

### iterative

stmt = """def factorial(num):
            return_value = 1;
            for i in range(2, num + 1):
                return_value *= i
            return return_value
            """
print("Iterative:", timeit('factorial(5)', setup = stmt, number=1000000))

### reduce
stmt = """from functools import reduce
def fact_with_reduce(num):
    return reduce(lambda x,y:x*y, range(1,num+1) or [1])
"""

print("Reduce:", timeit('fact_with_reduce(5)', setup = stmt, number=1000000))

### math

stmt = """from math import factorial
"""

print("Math:", timeit('factorial(5)', setup = stmt, number=1000000))