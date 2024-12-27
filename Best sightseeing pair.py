from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i = values[0] 
        for j in range(1, len(values)):
            max_score = max(max_score, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)

        return max_score
solution = Solution()
values1 = [8, 1, 5, 2, 6]
values2 = [1, 2]
print(solution.maxScoreSightseeingPair(values1))  
print(solution.maxScoreSightseeingPair(values2)) 
