# Problem: Assign Cookies
# Goal: Maximize the number of children who get a cookie.
# Each child can have at most one cookie, and a cookie can only be given to a child
# if the cookie’s size is ≥ the child’s greed factor.

# Example:
# Children’s greed factors: [1, 2, 3]
# Cookie sizes: [1, 1, 2]
# Solution: 2 children can be satisfied (child 1 gets cookie 1, child 2 gets cookie 3).
from typing import List


class Solution:
    def assign_cookies(self, greed: List[int], cookies: List[int]) -> int:
        greed.sort()
        cookies.sort()
        child = 0
        cookie = 0
        m = len(greed)
        n = len(cookies)

        while child < m and cookie < n:
            if cookies[cookie] >= greed[child]:
                child += 1
            cookie += 1
        return child


sol = Solution()
greed = [1, 2, 3]
cookies = [1, 1, 2]
print(sol.assign_cookies(greed, cookies))
