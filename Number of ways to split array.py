from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits
solution = Solution()
nums1 = [10, 4, -8, 7]
print(solution.waysToSplitArray(nums1))  
nums2 = [2, 3, 1, 0]
print(solution.waysToSplitArray(nums2)) 
