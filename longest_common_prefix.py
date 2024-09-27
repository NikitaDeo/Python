from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start by assuming the entire first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix size until it matches the start of the current string
            while not s.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # If there's no common prefix, return an empty string
        
        return prefix

# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""