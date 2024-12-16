from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums
solution = Solution()
nums1 = [2, 1, 3, 5, 6]
k1 = 5
multiplier1 = 2
print(solution.getFinalState(nums1, k1, multiplier1)) 
nums2 = [1, 2]
k2 = 3
multiplier2 = 4
print(solution.getFinalState(nums2, k2, multiplier2)) 
