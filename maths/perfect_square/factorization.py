def factor(num):
    if num == 1:
        return [1]
    if num == 2:
        return [2]
    if num < 0:
        return []
    primes = []

    while num % 2 == 0:
        primes.append(2)
        num //= 2

    for d in range(3, int(num**0.5) + 1, 2):
        while num % d == 0:
            primes.append(d)
            num //= d

    if num > 1:
        primes.append(num)

    return primes


'''
primes = [2,3,5,7,11,13,17,19,23,29]
num = 1

for n in primes:
    num *= n

# num += 1
num = 16

print(f'factors of {num}\n{factor(num)}')
'''
