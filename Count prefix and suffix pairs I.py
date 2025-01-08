from typing import List

class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count
solution = Solution()
words1 = ["a", "aba", "ababa", "aa"]
words2 = ["pa", "papa", "ma", "mama"]
words3 = ["abab", "ab"]

print(solution.countPrefixSuffixPairs(words1)) 
print(solution.countPrefixSuffixPairs(words2))
print(solution.countPrefixSuffixPairs(words3))     
