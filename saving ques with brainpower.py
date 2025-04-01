class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points = questions[i][0]
            skip = questions[i][1]
            solve = points + dp[i + skip + 1] if i + skip + 1 < n + 1 else points
            skip_question = dp[i + 1]
            dp[i] = max(solve, skip_question)
        return dp[0]
