from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        result = 0
        freq = {}

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            result += right - left + 1

        return result 
