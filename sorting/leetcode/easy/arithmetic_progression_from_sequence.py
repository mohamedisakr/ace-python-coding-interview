from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort(reverse=True)
        consective_diff = arr[0] - arr[1]

        for i in range(1, n - 1):
            diff = arr[i] - arr[i + 1]
            if consective_diff != diff:
                return False

        return True


arr = [3, 5, 1]
my_sol = Solution()
print(my_sol.canMakeArithmeticProgression(arr))
