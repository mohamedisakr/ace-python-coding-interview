def factorial(n, acc=1):
    if n == 1:
        return acc

    return factorial(n-1, n*acc)
