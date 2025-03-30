from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        # Initialize variables for tracking partitions
        partitions = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # Update the end of the current partition
            end = max(end, last_occurrence[char])
            
            # If the current index matches the end of the partition
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        
        return partitions
