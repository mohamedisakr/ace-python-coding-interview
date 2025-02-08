def from_base_to_base10(number: str, base: int) -> int:
    """
    Converts a number from a given base to base 10.

    :param number: The number as a string in the original base.
    :param base: The base of the original number (e.g., 2 for binary, 16 for hexadecimal).
    :return: The base 10 equivalent as an integer.
    """
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36")

    base10_num = 0
    for i, digit in enumerate(reversed(number)):
        if '0' <= digit <= '9':
            val = ord(digit) - ord('0')
        elif 'A' <= digit.upper() <= 'Z':
            val = ord(digit.upper()) - ord('A') + 10
        else:
            raise ValueError(
                "Invalid character in the number for the given base")

        if val >= base:
            raise ValueError(f"Digit {digit} is not valid for base {base}")

        base10_num += val * (base ** i)

    return base10_num


# Example usage:
# base_number = "1A3"  # Example number in base 16 (hexadecimal)
# base = 16  # Specifying the base
# base10_number = from_base_to_base10(base_number, base)
# print(base10_number)  # Outputs: 419


def to_base_7(num: int) -> int:
    if num == 0:
        return 0

    base_7 = ''
    while num:
        base_7 = str(num % 7) + base_7
        num //= 7

    return int(base_7)


def to_base_8(num: int) -> int:
    if num == 0:
        return 0
    base_8 = ''
    while num:
        base_8 = str(num % 8) + base_8
        num //= 8
    return int(base_8)


def to_base_9(num: int) -> int:
    if num == 0:
        return 0
    base_9 = ''
    while num:
        base_9 = str(num % 9) + base_9
        num //= 9
    return int(base_9)


num = 531440
print(to_base_9(num))  # correct: 888601

# num = 862
# print(to_7(num))

# num = 129
# print(to_8(num))

# def to_7(num: int):  # -> int:
#     b = 7
#     base_7 = []
#     while num:
#         base_7.append(num % b)
#         num //= b

#     return int("".join(str(n) for n in base_7[::-1]))
