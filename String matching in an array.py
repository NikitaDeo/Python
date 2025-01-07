from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.add(words[i]) 
        return list(result)
solution = Solution()
print(solution.stringMatching(["mass", "as", "hero", "superhero"]))
print(solution.stringMatching(["leetcode", "et", "code"]))  
print(solution.stringMatching(["blue", "green", "bu"]))  
print(solution.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"])) 
