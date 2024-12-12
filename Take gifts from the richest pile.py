import heapq
from math import isqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            max_gift = -heapq.heappop(max_heap)
            remaining_gifts = isqrt(max_gift)
            heapq.heappush(max_heap, -remaining_gifts)
        return -sum(max_heap)
