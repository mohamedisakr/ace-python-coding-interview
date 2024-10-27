"""
Question #1

In Python or C++, write an algorithm (function) for determining the parity of an integer, 
which will be similar to the one below in functionality, but different in essence. 
Explain the pros and cons of both implementations. 

Example: 
```
def isEven(value):
      return value % 2 == 0
```      
"""


def is_even(value: int) -> bool:
    """
    Determines whether an integer is even.

    Args:
        value (int): The integer to check.

    Returns:
        bool: True if the integer is even, False otherwise.

    Examples:
        >>> isEven(4)
        True
        >>> isEven(5)
        False
    """
    return (value & 1) == 0

# def isEven(value: int) -> bool:
#     length = ceil(log2(ceil(log2(value)+1)))
#     for i in range(length-1, -1, -1):
#         # print(2**i)
#         value ^= (value >> (2**i))
#     return value & 1


# value = 7
# print(f'Number {value} is: {'Odd' if isEven(value) else 'Even'}')

# arr = [1, 3, 5, 7, 9]
# for item in arr:
#     print(f'{item} is: {'Even' if isEven(item) else 'Odd'}')
