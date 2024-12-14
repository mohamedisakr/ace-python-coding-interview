# 170. Two Sum III - Data structure design
# https://leetcode.com/problems/two-sum-iii-data-structure-design/
from collections import Counter


class TwoSum:
    """Design a data structure that accepts a stream of integers and 
    checks if it has a pair of integers that sum up to a particular value
    """

    def __init__(self):
        """ Initializes the TwoSum object, with an empty array initially.
        """
        self.counter = Counter()

    def add(self, number: int):
        """Adds number to the data structure.
        """
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        """Returns true if there exists any pair of numbers whose sum is equal to value, 
        otherwise, it returns false.
        """
        for num in self.counter:
            complement = value - num
            if (complement != num and complement in self.counter) or (complement == num and self.counter[num] > 1):
                return True
        return False
