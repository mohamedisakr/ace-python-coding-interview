# What is the sum of the two smallest multiples of 6 that are greater than 103?
def sum_of_two(n: int) -> int:
    remainder = n % 6
    return (n + 5) + (n + 11)


n = 103
print(sum_of_two(n))
