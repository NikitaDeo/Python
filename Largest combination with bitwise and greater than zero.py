from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for bit in range(24):
            count = sum((num >> bit) & 1 for num in candidates)
            max_count = max(max_count, count)
        
        return max_count