from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result
solution = Solution()
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
print(solution.wordSubsets(words1, words2))  
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]
print(solution.wordSubsets(words1, words2)) 
