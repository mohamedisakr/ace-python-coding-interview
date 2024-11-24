# from string import ascii_lowercase
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numerical = self.convert_to_int(s)

        for _ in range(k):
            numerical = self.sum_digits(numerical)

        return numerical

    def sum_digits(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))

    def convert_to_int(self, s: str) -> int:
        return int(''.join(str(string.ascii_lowercase.index(char) + 1) for char in s))
