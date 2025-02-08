def sieve(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, num + 1, start):
                is_prime[multiple] = False
    return is_prime


def sieve_to_numbers(num: int):
    n = len(sieve(num))
    primes = []
    for i in range(n):
        if sieve(num)[i] == True:
            primes.append(i)
    return primes


# primes = sieve_to_numbers(100)
# print(primes)
# print(len(primes))
