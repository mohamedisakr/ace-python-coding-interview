def fibonacci_iter(nth_number):
    a, b = 1, 1
    print(f'a = {a}, b = {b}')

    for _ in range(1, nth_number):
        a, b = b, a + b  # Get the next Fibonacci number.
        print(f'a = {a}, b = {b}')
    return a


# print(fibonacci_iter(10))


def fibonacci(nth_number):
    print(f'fibonacci({nth_number}) called.')
    if nth_number == 1 or nth_number == 2:
        # BASE CASE
        print(f'Call to fibonacci({nth_number}) returning 1.')
        return 1
    else:
        # RECURSIVE CASE
        print(f'Calling fibonacci({nth_number -
              1}) and fibonacci({nth_number - 2}).')
        result = fibonacci(nth_number - 1) + fibonacci(nth_number - 2)
        print(f'Call to fibonacci({nth_number}) returning {result}.')
        return result


print(fibonacci(10))
