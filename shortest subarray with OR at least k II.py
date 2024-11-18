from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        or_value = 0
        left = 0
        
        for right in range(len(nums)):
            or_value |= nums[right]
            while or_value >= k and left <= right:
                min_length = min(min_length, right - left + 1)
                or_value ^= nums[left]
                left += 1
        return min_length if min_length != float('inf') else -1