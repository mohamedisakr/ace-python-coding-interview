# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


sol = Solution()
address = "255.100.50.0"
print(sol.defangIPaddr(address))
