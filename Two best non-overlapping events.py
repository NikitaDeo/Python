from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        max_val = [0] * n
        max_val[0] = events[0][2]
        for i in range(1, n):
            max_val[i] = max(max_val[i - 1], events[i][2])

        result = 0

        for i, (start, end, value) in enumerate(events):
            idx = bisect_right([e[1] for e in events], start - 1) - 1
            if idx >= 0:
                result = max(result, value + max_val[idx])
            else:
                result = max(result, value)

        return result            
