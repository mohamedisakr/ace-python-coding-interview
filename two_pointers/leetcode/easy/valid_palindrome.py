# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1

        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1

        return True


# Example usage:
solution = Solution()
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(solution.isPalindrome("race a car"))  # Output: False

print(solution.isPalindrome("kayak"))
print(solution.isPalindrome("deified"))
print(solution.isPalindrome("rotator"))
print(solution.isPalindrome("repaper"))
print(solution.isPalindrome("deed"))
print(solution.isPalindrome("peep"))
print(solution.isPalindrome("wow"))
print(solution.isPalindrome("noon"))
print(solution.isPalindrome("civic"))
print(solution.isPalindrome("racecar"))
print(solution.isPalindrome("level"))
print(solution.isPalindrome("mom"))
print(solution.isPalindrome("bird rib"))
print(solution.isPalindrome("taco cat"))
print(solution.isPalindrome("UFO tofu"))
print(solution.isPalindrome("Borrow or rob?"))
print(solution.isPalindrome("Never odd or even."))
