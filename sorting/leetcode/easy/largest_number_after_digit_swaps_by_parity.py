class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = list(str(num))  # Convert number to list of characters

        # Extract digits based on index positions
        even_positions = [i for i in range(
            len(num_str)) if int(num_str[i]) % 2 == 0]
        odd_positions = [i for i in range(
            len(num_str)) if int(num_str[i]) % 2 == 1]

        # Get even and odd digits and sort them in descending order
        even_digits = sorted([num_str[i]
                             for i in even_positions], reverse=True)
        odd_digits = sorted([num_str[i] for i in odd_positions], reverse=True)

        # Reconstruct the number while keeping original index parity
        result = list(num_str)  # Copy original structure
        even_idx, odd_idx = 0, 0

        for i in range(len(num_str)):
            if int(num_str[i]) % 2 == 0:  # Replace even-positioned digit
                result[i] = even_digits[even_idx]
                even_idx += 1
            else:  # Replace odd-positioned digit
                result[i] = odd_digits[odd_idx]
                odd_idx += 1

        return int("".join(result))  # Convert list back to integer


# Example usage:
solution = Solution()
print(solution.largestInteger(247))  # Expected Output: 427
print(solution.largestInteger(2736))  # Expected Output: 7236
print(solution.largestInteger(65875))  # Expected Output: 87655


# num = 1234
num = 65875
sol = Solution()
print(sol.largestInteger(num))

# class Solution:
#     def largestInteger(self, num: int) -> int:
#         num_str = list(str(num))
#         n = len(num_str)

#         even_indices = [num_str[i] for i in range(n) if i % 2 == 0]
#         odd_indices = [num_str[i] for i in range(n) if i % 2 != 0]

#         even_indices.sort(reverse=True)
#         odd_indices.sort(reverse=True)

#         even, odd = 0, 0
#         max_num = []

#         for i in range(n):
#             if i % 2 == 0:
#                 max_num.append(even_indices[even])
#                 even += 1
#             else:
#                 max_num.append(odd_indices[odd])
#                 odd += 1

#         return int(''.join(max_num))
