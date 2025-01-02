class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        def is_vowel_string(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return word[0] in vowels and word[-1] in vowels
        n = len(words)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_string(words[i]) else 0)
        result = []
        for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])

        return result
solution = Solution()
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
print(solution.vowelStrings(words, queries)) 
