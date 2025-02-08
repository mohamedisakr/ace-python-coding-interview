def oct_to_decimal(num):
    exp = 0
    decimal = 0
    while num:
        digit = num % 10
        decimal += digit*(8 ** exp)
        num //= 10
        exp += 1
    return decimal


def hex_to_decimal(s):
    letter_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    exp = 0
    decimal = 0
    for char in s[::-1]:
        # 'DA6'
        # case 1: letter
        if char in letter_map:
            decimal += letter_map[char] * (16 ** exp)
        # case 2: number
        else:
            decimal += int(char) * (8 ** exp)
        exp += 1
    return decimal


# base_8 = [23, 62, 471, 266]
# for num in base_8:
#     print(f'{num} in base 8 is {oct_to_decimal(num)} in base 10')


base_16 = ['286', '591', '4A', 'C7', 'DA6', '1B4']
for num in base_16:
    print(f'{num} in base 16 is {hex_to_decimal(num)} in base 10')
