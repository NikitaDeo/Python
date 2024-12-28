from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum

        for i in range(1, n - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            window_sum[i] = current_sum
        left_max = [0] * len(window_sum)
        max_index = 0

        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[max_index]:
                max_index = i
            left_max[i] = max_index
        right_max = [0] * len(window_sum)
        max_index = len(window_sum) - 1

        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[max_index]:
                max_index = i
            right_max[i] = max_index
        max_total = 0
        result = [-1, -1, -1]

        for mid in range(k, len(window_sum) - k):
            left = left_max[mid - k]
            right = right_max[mid + k]
            total = window_sum[left] + window_sum[mid] + window_sum[right]

            if total > max_total:
                max_total = total
                result = [left, mid, right]

        return result
solution = Solution()
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(solution.maxSumOfThreeSubarrays(nums, k))  
