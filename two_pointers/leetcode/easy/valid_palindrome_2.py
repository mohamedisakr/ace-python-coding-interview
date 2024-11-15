class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(lo, hi):
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo, hi = lo + 1, hi - 1
            return True

        lo = 0
        hi = len(s)-1

        while lo < hi:
            if s[lo] != s[hi]:
                return is_palindrome(lo, hi-1) or is_palindrome(lo+1, hi)
            lo, hi = lo + 1, hi - 1
        return True
