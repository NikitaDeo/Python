class Solution:
    def maximumLength(self, s: str) -> int:
        def is_special(sub):
            return len(set(sub)) == 1

        n = len(s)
        result = -1

        for length in range(1, n + 1):
            count = {}
            for i in range(n - length + 1):
                sub = s[i:i + length]
                if is_special(sub):
                    count[sub] = count.get(sub, 0) + 1
                    if count[sub] >= 3:
                        result = max(result, length)

        return result

solution = Solution()
print(solution.maximumLength("aaaa")) 
print(solution.maximumLength("abcdef")) 
print(solution.maximumLength("abcaba")) 
