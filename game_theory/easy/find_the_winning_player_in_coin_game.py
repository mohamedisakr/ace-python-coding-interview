# 3222. Find the Winning Player in Coin Game
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        return 'Bob' if min(x, y // 4) % 2 == 0 else 'Alice'
