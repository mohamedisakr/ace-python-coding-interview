# 170. Two Sum III - Data structure design
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

from collections import Counter


class TwoSum:
    def __init__(self):
        self.counter = Counter()

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        for num in self.counter:
            complement = value - num
            if complement in self.counter:
                if complement != num or self.counter[num] > 1:
                    return True
        return False


# Example usage:
two_sum = TwoSum()
two_sum.add(1)
two_sum.add(3)
two_sum.add(5)
print(two_sum.find(4))  # Output: True
print(two_sum.find(7))  # Output: False
