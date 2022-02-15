def first_n_fib(n):
    fib = [0] * n
    fib[0] = fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib
