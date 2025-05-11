from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        total_xor_sum = 0
        # Iterate through bit positions (0 to 30, as constraints imply numbers < 2^31)
        for i in range(31):
            count_set_bits = 0
            for num in nums:
                if (num >> i) & 1:
                    count_set_bits += 1

            if count_set_bits > 0:
                # For each bit position with at least one '1', there are 2^(n-1) subsets
                # that will have a '1' at this bit position in their XOR sum.
                total_xor_sum += (1 << i) * (1 << (n - 1))

        return total_xor_sum

        # n = len(nums)
        # total = 0

        # for num in nums:
        #     total ^= num

        # return total * (2 ** (n - 1))
