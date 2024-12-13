from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False] * len(nums)
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))

        score = 0

        for num, index in indexed_nums:
            if marked[index]:
                continue
            score += num
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < len(nums) - 1:
                marked[index + 1] = True

        return score 
