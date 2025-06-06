# What is the largest multiple of 73 that is less than 2000?

def largest_multiple(n: int) -> int:
    return n - (n % 73)


n = 2000
print(largest_multiple(n))
