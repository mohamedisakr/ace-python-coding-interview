from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for index, _ in enumerate(seats):
            moves += abs(seats[index] - students[index])

        return moves
