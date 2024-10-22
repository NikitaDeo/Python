class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, it's impossible to find a permutation
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for s1 and the current window in s2
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Helper function to convert a character to its corresponding index
        def char_to_index(c):
            return ord(c) - ord('a')
        
        # Fill the frequency array for s1
        for char in s1:
            s1_count[char_to_index(char)] += 1
        
        # Initialize the first window of size len(s1) in s2
        for i in range(len(s1)):
            s2_count[char_to_index(s2[i])] += 1
        
        # Compare the first window
        if s1_count == s2_count:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character (right side of the window)
            s2_count[char_to_index(s2[i])] += 1
            # Remove the old character (left side of the window)
            s2_count[char_to_index(s2[i - len(s1)])] -= 1
            
            # Compare the counts again
            if s1_count == s2_count:
                return True
        
        return False