# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""
        while columnNumber > 0:
            offset = (columnNumber-1) % 26
            column_title += chr(ord('A') + offset)
            columnNumber = (columnNumber-1) // 26
        return column_title[::-1]
