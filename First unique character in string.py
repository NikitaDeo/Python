from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index 
        return -1 