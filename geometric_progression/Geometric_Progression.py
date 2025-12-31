from functools import lru_cache
from typing import List, Union


class GeometricProgression:
    # def __init__(self, series: List[Union[int, float]]):
    #     if len(series) < 2:
    #         raise ValueError("Series must contain at least two elements.")

    #     self.a = series[0]
    #     # Using a small epsilon check for floating point stability can be added here
    #     self.r = series[1] / series[0]

    def __init__(self, a, r):
        self.a = a
        self.r = r

    @lru_cache(maxsize=128)
    def get_term(self, n: int) -> float:
        """
        Calculates the n-th term. 
        Time: O(log n)
        Space: O(1) [excluding cache]
        """
        if n < 1:
            raise ValueError("n must be a positive integer.")
        return self.a * (self.r ** (n - 1))

    def get_sum(self, n: int) -> float:
        """
        Calculates the sum of first n terms.
        Time: O(log n)
        """
        if n < 1:
            raise ValueError("n must be a positive integer.")
        if self.r == 1:
            return self.a * n

        # Standard formula: a(r^n - 1) / (r - 1)
        # return self.a * (pow(self.r, n) - 1) / (self.r - 1)
        return self.a * (self.r**n - 1) / (self.r - 1)

    @classmethod
    def from_two_terms(cls, n1, val1, n2, val2):
        """
        Creates a GP instance from any two terms.
        val1 is the n1-th term, val2 is the n2-th term.
        """
        # val2 / val1 = (a * r^(n2-1)) / (a * r^(n1-1)) = r^(n2 - n1)
        r = (val2 / val1) ** (1 / (n2 - n1))
        a = val1 / (r ** (n1 - 1))
        return cls(a, r)


gp = GeometricProgression.from_two_terms(n1=1, val1=4, n2=6, val2=128)

print(f"8th term: {gp.get_term(8)}")   # Output: 512.0
print(f"11th term: {gp.get_term(11)}")  # Output: 4096.0

# non-optimized version
# class GeometricProgression:
#     def __init__(self, series):
#         """Initializes the GP by extracting a and r from a provided list."""
#         if len(series) < 2:
#             raise ValueError("Series must contain at least two elements.")
#         self.a = series[0]
#         self.r = series[1] / series[0]
#         self.series = series

#     def get_term(self, n):
#         """Calculates the n-th term: a * r^(n-1)"""
#         return self.a * (self.r ** (n - 1))

#     def get_sum(self, n):
#         """Calculates the sum of the first n terms."""
#         if self.r == 1:
#             return self.a * n
#         return self.a * (self.r**n - 1) / (self.r - 1)

#     def __repr__(self):
#         return f"GP(a={self.a}, r={self.r})"
