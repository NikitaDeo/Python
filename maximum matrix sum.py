from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_value = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_value = min(min_value, abs(val))
        if negative_count % 2 == 1:
            total_sum -= 2 * min_value

        return total_sum
