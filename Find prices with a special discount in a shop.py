from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break

        return result

solution = Solution()
prices1 = [8, 4, 6, 2, 3]
prices2 = [1, 2, 3, 4, 5]
prices3 = [10, 1, 1, 6]

print(solution.finalPrices(prices1))  
print(solution.finalPrices(prices2)) 
print(solution.finalPrices(prices3)) 
