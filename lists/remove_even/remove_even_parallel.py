
from concurrent.futures import ProcessPoolExecutor


def is_odd(x):
    return x % 2 != 0


def remove_even(lst):
    with ProcessPoolExecutor() as executor:
        result = list(executor.map(is_odd, lst))
    return [x for x, keep in zip(lst, result) if keep]


if __name__ == "__main__":
    my_list = [1, 2, 4, 5, 10, 6, 3]
    print(remove_even(my_list))
