# What is the units digit (ones digit) of the product of any six consecutive positive integers?
def unit_digit_product_of_6(n: int) -> int:
    # 1, 2, 3, 4, 5, 6
    total = 1
    num_of_ints = 6
    for i in range(num_of_ints):
        print(n+i)
        total *= (n + i)
    return total


n = 5
print(unit_digit_product_of_6(n))
