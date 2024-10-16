import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        
        min_heap = []
        max_value = float('-inf')
        
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0)) 
            
            max_value = max(max_value, nums[i][0])
            
        range_start, range_end = float('-inf'), float('inf')
        
        while min_heap:
            min_value, row, col = heapq.heappop(min_heap)
            

            if max_value - min_value < range_end - range_start:
                range_start, range_end = min_value, max_value
            

            if col + 1 < len(nums[row]):
                next_value = nums[row][col + 1]
                heapq.heappush(min_heap, (next_value, row, col + 1))
                max_value = max(max_value, next_value)
            else:

                break
        
        return [range_start, range_end]