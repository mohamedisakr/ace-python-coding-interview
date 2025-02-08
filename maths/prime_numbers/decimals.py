def to_7(num: int) -> int:
    if num == 0:
        return 0

    base_7 = ''
    while num:
        base_7 = str(num % 7) + base_7
        num //= 7

    return int(base_7)


num = 862
print(to_7(num))

# def to_7(num: int):  # -> int:
#     b = 7
#     base_7 = []
#     while num:
#         base_7.append(num % b)
#         num //= b

#     return int("".join(str(n) for n in base_7[::-1]))
