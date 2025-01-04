class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        unique_palindromes = set()
        for char in first_occurrence:
            if first_occurrence[char] < last_occurrence[char]:
                middle_chars = set(s[first_occurrence[char] + 1:last_occurrence[char]])
                for mid_char in middle_chars:
                    unique_palindromes.add(char + mid_char + char)

        return len(unique_palindromes)
solution = Solution()
print(solution.countPalindromicSubsequence("aabca")) 
print(solution.countPalindromicSubsequence("adc"))
print(solution.countPalindromicSubsequence("bbcbaba")) 
