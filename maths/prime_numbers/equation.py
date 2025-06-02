# Suppose P and Q both represent prime numbers such that
# 5P + 7Q = 109
# Find the value of the prime P.
primes_up_to_150 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                    61, 67, 71, 73, 79, 83,	89,	97, 101, 103, 107, 109, 113, 127,
                    131, 137, 139, 149]
for i, p in enumerate(primes_up_to_150):
    for j, q in enumerate(primes_up_to_150):
        if p != q:
            print(f'P: {p}, Q: {q}')
            if 5*p + 7*q == 109:
                print(f'Result founded P: {p}, Q: {q}')
                break
