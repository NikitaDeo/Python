class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        if words[-1][-1] != words[0][0]:
            return False
        
        return True
solution = Solution()
print(solution.isCircularSentence("leetcode exercises sound delightful"))
print(solution.isCircularSentence("eetcode"))  
print(solution.isCircularSentence("Leetcode is cool"))  