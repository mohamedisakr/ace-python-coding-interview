"""
https://leetcode.com/discuss/interview-question/5988967/amazon-sde-i-india-online-assessment

Code Question 2
In Amazon's online marketplace, the inventory manager is exploring strategies to enhance 
product sales. The focus is on creating appealing packages the offer customers a delightful 
shoppinig experience. 

To achieve this, the inventory manager aims to construct packages, 
each containing at most 2 items, to have equal total cost across all packages. 

The total cost of a package is defined as the sum of the costs of the items contained within.


Formally, given an array cost of size n, representing the cost of individual items, determine 
the maximum number of packages that can be created, such that each package adheres to the 
constraint of having at most 2 items, and all packages have the same cost.


Note that each item can be used in at most one package.


Examples:


cost = [2, 1, 3]
ans = 2

cost = [4, 5, 10, 3, 1, 2, 2, 2, 3]
ans = 4

cost = [1, 1, 2, 2, 1, 4]
ans = 3

cost = [10, 2, 1]
ans = 1

Constraints:

1 <= n <= 2 * 10^5
1 <= cost[i] <= 2000
"""


from collections import defaultdict


def find_max_packages(cost: list[int]) -> int:
    cost.sort()  # Step 1: Sort the costs
    frequencies = defaultdict(int)

    # Counting single items
    for item in cost:
        frequencies[item] += 1

    # Use two-pointer technique for pairs
    left, right = 0, len(cost) - 1
    while left < right:
        pair_cost = cost[left] + cost[right]
        frequencies[pair_cost] += 1
        left += 1
        right -= 1

    # Calculate maximum packages from frequencies
    max_packages = max(frequencies.values()) if frequencies else 0

    return max_packages


# Example usage
cost = [2, 1, 3]
print(find_max_packages(cost))  # Should return 2

cost = [4, 5, 10, 3, 1, 2, 2, 2, 3]
print(find_max_packages(cost))  # Should return 4

cost = [1, 1, 2, 2, 1, 4]
print(find_max_packages(cost))  # Should return 3

cost = [10, 2, 1]
print(find_max_packages(cost))  # Should return 1
