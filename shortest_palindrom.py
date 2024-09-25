class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return s
     
        s_rev = s[::-1]
        new_str = s + "#" + s_rev
        n = len(new_str)
        lps = [0] * n 
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and new_str[i] != new_str[j]:
                j = lps[j - 1]
            if new_str[i] == new_str[j]:
                j += 1
            lps[i] = j       
        longest_palindromic_prefix_length = lps[-1]
     
        to_add = s[longest_palindromic_prefix_length:][::-1]
        
        return to_add + s

solution = Solution()

print(solution.shortestPalindrome("aacecaaa"))
print(solution.shortestPalindrome("abcd"))