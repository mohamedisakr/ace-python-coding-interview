def to_binary(num: int) -> str:
    if num == 0:
        return '0'
    if num == 1:
        return '1'

    i = 0
    res = [''] * (num.bit_length())
    # print(f'{num} bit length: {num.bit_length()}')
    while num > 0:
        res[- 1 - i] = str(num % 2)
        num //= 2
        i += 1

    return ''.join(res)


num = 1507
print(to_binary(num))

# def to_binary(num: int) -> str:
#     if num == 0:
#         return '0'

#     res = ''
#     while num > 0:
#         res = str(num % 2) + res
#         num //= 2

#     return res
