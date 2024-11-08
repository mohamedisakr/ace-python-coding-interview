# https://leetcode.com/problems/number-of-recent-calls/description/
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
from collections import deque


class RecentCounter:
    def __init__(self):
        self._queue = deque()

    def ping(self, t: int) -> int:
        self._queue.append(t)
        while self._queue[0] < t-3000:
            self._queue.popleft()
        return len(self._queue)

# recentCounter = RecentCounter()
# recentCounter.ping(1)  # requests = [1], range is [-2999, 1], return 1
# recentCounter.ping(100)  # requests = [1, 100], range is [-2900, 100], return 2
# # requests = [1, 100, 3001], range is [1, 3001], return 3
# recentCounter.ping(3001)
# # requests = [1, 100, 3001, 3002], range is [2, 3002], return 3
# recentCounter.ping(3002)
