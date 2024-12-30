class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]
                dp[length] %= MOD
            if length >= one:
                dp[length] += dp[length - one]
                dp[length] %= MOD
        result = sum(dp[low:high + 1]) % MOD

        return result
solution = Solution()
print(solution.countGoodStrings(3, 3, 1, 1)) 
print(solution.countGoodStrings(2, 3, 1, 2)) 
        
