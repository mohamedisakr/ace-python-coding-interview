# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m, n = len(players), len(trainers)
        i, j = 0, 0
        matchings = 0

        players.sort()
        trainers.sort()

        while i < m and j < n:
            if players[i] <= trainers[j]:
                matchings += 1
                i += 1
                j += 1
            else:
                j += 1

        return matchings
