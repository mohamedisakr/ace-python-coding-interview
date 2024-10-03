import math


def remove_even(lst):
    for x in lst:
        if x is None or (isinstance(x, float) and math.isnan(x)):
            raise TypeError("List contains invalid elements")
        if not isinstance(x, (int, float)):
            raise TypeError("List contains invalid elements")
    return [x for x in lst if isinstance(x, (int, float)) and x % 2 != 0]
