from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        dp = [0] * (days[-1] + 1)

        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0], 
                    dp[max(0, day - 7)] + costs[1], 
                    dp[max(0, day - 30)] + costs[2]  
                )

        return dp[days[-1]]
solution = Solution()
print(solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(solution.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))     
