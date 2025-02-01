# 1710. Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/description/

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda arr: -arr[1])
        print(boxTypes)
        total_units = 0

        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            total_units += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total_units


sol = Solution()
boxTypes, truckSize = [[5, 10], [2, 5], [4, 7], [3, 9]], 10
print(sol.maximumUnits(boxTypes, truckSize))
