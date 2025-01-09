from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count
solution = Solution()
print(solution.prefixCount(["pay","attention","practice","attend"], "at"))
print(solution.prefixCount(["leetcode","win","loops","success"], "code"))
