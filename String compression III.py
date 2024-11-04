class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        while i < n:
            count = 1
            char = word[i]
            while i + 1 < n and word[i + 1] == char and count < 9:
                i += 1
                count += 1
            comp += str(count) + char
            i += 1
        return comp
solution = Solution()
print(solution.compressedString("abcde")) 
print(solution.compressedString("aaaaaaaaaaaaaabb")) 