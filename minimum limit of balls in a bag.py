from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDistribute(maxPenalty: int) -> bool:
            operations = 0
            for num in nums:
                if num > maxPenalty:
                    operations += (num - 1) // maxPenalty
            return operations <= maxOperations
        left, right = 1, max(nums) 
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid 
            else:
                left = mid + 1 
        return left
