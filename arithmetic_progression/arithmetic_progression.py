from functools import lru_cache
from typing import List, Union


class ArithmeticProgression:
    def __init__(self, series: List[Union[int, float]]):
        if len(series) < 2:
            raise ValueError("Series must contain at least two elements.")

        self.a = series[0]
        # Calculate common difference (d) instead of ratio (r)
        self.d = series[1] - series[0]
        self.series = series

    @lru_cache(maxsize=128)
    def get_term(self, n: int) -> float:
        """
        Calculates the n-th term: a + (n - 1)d
        Time: O(1)
        """
        if n < 1:
            raise ValueError("n must be a positive integer.")
        return self.a + (n - 1) * self.d

    def get_sum(self, n: int) -> float:
        """
        Calculates the sum of first n terms: (n/2) * [2a + (n - 1)d]
        Time: O(1)
        """
        if n < 1:
            raise ValueError("n must be a positive integer.")
        # Formula: n/2 * (first_term + last_term)
        return (n / 2) * (2 * self.a + (n - 1) * self.d)

    def __repr__(self):
        return f"AP(a={self.a}, d={self.d})"


# --- Usage Example ---
# Series: 5, 10, 15, 20... (d = 5)
ap = ArithmeticProgression([5, 10, 15, 20])


print(f"Series: {ap.series}")  # 5 + (99 * 5) = 500
print(f"100th Term: {ap.get_term(100)}")  # 5 + (99 * 5) = 500
print(f"Sum of first 10 terms: {ap.get_sum(10)}")  # (10/2) * (10 + 45) = 275
