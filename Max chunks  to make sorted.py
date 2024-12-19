from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        chunks = 0

        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])
           
            if max_so_far == i:
                chunks += 1

        return chunks

solution = Solution()
arr1 = [4, 3, 2, 1, 0]
arr2 = [1, 0, 2, 3, 4]

print(solution.maxChunksToSorted(arr1))  
print(solution.maxChunksToSorted(arr2)) 
