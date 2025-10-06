from typing import List, Callable


def all_true(n, function_list):
    """ 
    n is an int
    function_list is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in function_list returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    return all(f(n) for f in function_list)


def is_even(x):
    return x % 2 == 0


def is_positive(x):
    return x > 0


def less_than_ten(x):
    return x < 100


Lf = [is_even, is_positive, less_than_ten]

# print(all_true(6, Lf))  # ✅ True
# print(all_true(98, Lf))  # ✅ True
# print(all_true(11, Lf))  # ❌ False (fails less_than_ten)
# print(all_true(-2, Lf))  # ❌ False (fails is_positive)


def all_true_verbose(n: int, function_list: List[Callable]) -> tuple[bool, List[int]]:
    """
    Evaluates a list of Boolean-returning functions on input n.

    Parameters:
        n (int): The input value to validate.
        function_list (list[callable]): A list of functions that take an int and return a Boolean.

    Returns:
        tuple[bool, list[int]]: 
            - First element is True if all functions return True, else False.
            - Second element is a list of indices of functions that failed.

    Time Complexity:
        O(k) — where k is the number of functions.
    Space Complexity:
        O(f) — where f is the number of failing functions.
    Auxiliary Space:
        O(1) — aside from the failure list.

    Optimization Grade Insight:
        - Short-circuiting can be disabled to collect full failure trace.
        - Ideal for validator pipelines, form checks, or rule engines.
    """
    failed = [i for i, f in enumerate(function_list) if not f(n)]
    return (len(failed) == 0, failed)


# def is_even(x): return x % 2 == 0
# def is_positive(x): return x > 0
# def less_than_ten(x): return x < 10


# validators = [is_even, is_positive, less_than_ten]

# print(all_true_verbose(6, validators))   # ✅ (True, [])
# print(all_true_verbose(11, validators))  # ❌ (False, [0, 2])
# print(all_true_verbose(-2, validators))  # ❌ (False, [1])


def validate_input(n: int, validators: dict[str, Callable]) -> dict:
    """
    Validates input n against a dictionary of named Boolean functions.

    Returns:
        dict: {
            'valid': bool,
            'failed': list[str]
        }
    """
    failed = [name for name, f in validators.items() if not f(n)]
    return {
        'valid': len(failed) == 0,
        'failed': failed
    }


rules = {
    "is_even": lambda x: x % 2 == 0,
    "is_positive": lambda x: x > 0,
    "less_than_ten": lambda x: x < 10
}

print(validate_input(6, rules))   # ✅ {'valid': True, 'failed': []}
# ❌ {'valid': False, 'failed': ['is_even', 'less_than_ten']}
print(validate_input(11, rules))
