from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        is_different = [0] * (n - 1)
        for i in range(n - 1):
            is_different[i] = 1 if (nums[i] % 2) != (nums[i + 1] % 2) else 0
        prefix_sum = [0] * (n - 1)
        for i in range(n - 1):
            prefix_sum[i] = prefix_sum[i - 1] + is_different[i] if i > 0 else is_different[i]
        result = []
        for from_i, to_i in queries:
            if to_i - from_i < 1:
                result.append(True)
                continue
            total_diff = prefix_sum[to_i - 1] - (prefix_sum[from_i - 1] if from_i > 0 else 0)
            result.append(total_diff == (to_i - from_i))
        
        return result
nums = [586, 1823, 586, 1823, 586, 1823]
queries = [[0, 4], [0, 5]]
solution = Solution()
output = solution.isArraySpecial(nums, queries)
print(output)
