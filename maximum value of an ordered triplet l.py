from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0  # Initialize the maximum value as 0
        n = len(nums)
        
        for i in range(n - 2):  # First index
            for j in range(i + 1, n - 1):  # Second index
                for k in range(j + 1, n):  # Third index
                    triplet_value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, triplet_value)
        
        return max_value
