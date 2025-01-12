class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        open_count = 0  
        flexible_count = 0 
        for i in range(len(s)):
            if locked[i] == '0':
                flexible_count += 1
            elif s[i] == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    open_count += 1
                else:
                    return False
        close_count = 0 
        flexible_count = 0 
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                flexible_count += 1
            elif s[i] == ')':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    close_count += 1
                else:
                    return False
        return True
solution = Solution()
print(solution.canBeValid(")())()", "010100")) 
print(solution.canBeValid("()()", "0000"))   
print(solution.canBeValid(")", "0"))   
