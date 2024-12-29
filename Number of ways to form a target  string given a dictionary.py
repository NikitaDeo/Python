from collections import Counter
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def numWays(self, words, target):
        m, n = len(target), len(words[0])
        char_count = [Counter() for _ in range(n)]
        for word in words:
            for col, char in enumerate(word):
                char_count[col][char] += 1
        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return 1
            if j == n:
                return 0
            result = dp(i, j + 1)
            if target[i] in char_count[j]:
                result += char_count[j][target[i]] * dp(i + 1, j + 1)
                result %= MOD

            return result

        return dp(0, 0)
solution = Solution()
words1 = ["acca", "bbbb", "caca"]
target1 = "aba"
print(solution.numWays(words1, target1)) 
words2 = ["abba", "baab"]
target2 = "bab"
print(solution.numWays(words2, target2)) 
