class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        prev = 0
        for space in spaces:
            result.append(s[prev:space])
            result.append(" ")
            prev = space
        result.append(s[prev:])
        return "".join(result)
solution = Solution()
print(solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
print(solution.addSpaces("icodeinpython", [1, 5, 7, 9]))   
print(solution.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6])) 
