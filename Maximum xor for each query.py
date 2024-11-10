from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (1 << maximumBit) - 1
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        result = []
        for num in reversed(nums):
            k = xor_all ^ max_val
            result.append(k)
            
            xor_all ^= num
        
        return result 