Fib = [0] * 1000
Fib[1] = Fib[2] = 1


def fib_rec(n):
    if not Fib[n]:
        Fib[n] = fib_rec(n - 1) + fib_rec(n - 2)
    return Fib[n]


def fib_lin(n):
    for i in range(3, n + 1):
        Fib[i] = Fib[i - 1] + Fib[i - 2]
    return Fib[n]
