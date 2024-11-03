class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
solution = Solution()
print(solution.rotateString("abcde", "cdeab")) 
print(solution.rotateString("abcde", "abced"))
