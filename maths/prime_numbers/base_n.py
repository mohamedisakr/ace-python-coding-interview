def oct_to_decimal(num):
    exp = 0
    decimal = 0
    while num:
        digit = num % 10
        decimal += digit*(8 ** exp)
        num //= 10
        exp += 1
    return decimal


base_8 = [23, 62, 471, 266]
for num in base_8:
    print(f'{num} in base 8 is {oct_to_decimal(num)} in base 10')

# num = 23
# print(oct_to_decimal(num))
