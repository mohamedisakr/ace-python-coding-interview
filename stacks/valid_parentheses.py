# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False

        return not stack
