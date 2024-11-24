class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            hi = x % 10
            lo = x // div

            if lo != hi:
                return False

            x = (x % div) // 10
            div = div / 100

        return True
