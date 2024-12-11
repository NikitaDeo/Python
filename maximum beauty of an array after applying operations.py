from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ranges = [(num - k, num + k) for num in nums]
        ranges.sort()

        max_beauty = 0
        window = []

        for start, end in ranges:
            while window and window[0] < start:
                window.pop(0)

            window.append(end)

            max_beauty = max(max_beauty, len(window))

        return max_beauty

solution = Solution()
nums1 = [4, 6, 1, 2]
k1 = 2
print(solution.maximumBeauty(nums1, k1)) 

nums2 = [1, 1, 1, 1]
k2 = 10
print(solution.maximumBeauty(nums2, k2)) 
