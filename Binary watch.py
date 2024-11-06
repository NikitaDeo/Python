from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible_times = []
        for hour in range(12): 
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    possible_times.append(f"{hour}:{minute:02d}")
        
        return possible_times 