### naive fibonacci

def fibonacci_iter(n):
    if n < 0:
        raise ValueError('n must be >0')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n -1):
            c = a + b
            a = b
            b = c
        return b

print("iterative:",fibonacci_iter(9))


## recursive fibonacci

def fibonacci_rec(n):
    if n < 0:
        raise ValueError('n must be >0')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1)+ fibonacci_rec(n-2)

print("Recursive:", fibonacci_rec(9))

# Мемоизация - это способ запоминания результатов функций, чтобы избежать повтороного вычисления тех же самых значений

cache = {0:0, 1:1}

def fibonacci_mem(num):
    #base case
    if num in cache:
        return cache[num]
    #cache fib num
    cache[num] = fibonacci_mem(num-1)+fibonacci_mem(num-2)
    return cache[num]

print([fibonacci_mem(num) for num in range(12)])
