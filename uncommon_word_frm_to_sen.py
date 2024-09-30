from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        count_s1 = Counter(s1.split())
        count_s2 = Counter(s2.split())
        combined_count = count_s1 + count_s2
        uncommon_words = [word for word in combined_count if combined_count[word] == 1]
        
        return uncommon_words
solution = Solution()

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(solution.uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(solution.uncommonFromSentences(s1, s2))