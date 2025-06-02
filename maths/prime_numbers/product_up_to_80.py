primes_up_to_80 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                   31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
prod = 1
for i, p in enumerate(primes_up_to_80):
    prod *= p
    if prod % 4 == 0:
        print(p)
        break
print(prod % 4)
