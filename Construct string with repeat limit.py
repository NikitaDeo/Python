import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))
            
        result = []
        prev_char = None 
        prev_count = 0  
        
        while max_heap:
            neg_ascii, count = heapq.heappop(max_heap)
            char = chr(-neg_ascii)
            if char == prev_char and prev_count >= repeatLimit:
                if not max_heap:
                     break 
                next_neg_ascii, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_neg_ascii)
                result.append(next_char)
                if next_count > 1:
                    heapq.heappush(max_heap, (next_neg_ascii, next_count - 1))
                heapq.heappush(max_heap, (neg_ascii, count))
                prev_char = next_char
                prev_count = 1
            else:
            
                can_add = min(count, repeatLimit if char != prev_char else repeatLimit - prev_count)
                result.append(char * can_add)
                count -= can_add
                if char == prev_char:
                    prev_count += can_add
                else:
                    prev_char = char
                    prev_count = can_add
                if count > 0:
                    heapq.heappush(max_heap, (neg_ascii, count))
        
        return ''.join(result)
solution = Solution()
print(solution.repeatLimitedString("cczazcc", 3)) 
print(solution.repeatLimitedString("aababab", 2)) 
