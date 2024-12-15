import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        max_heap = [(-gain(passed, total), passed, total) for passed, total in classes]
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            g, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            heapq.heappush(max_heap, (-gain(passed, total), passed, total))
        total_ratio = sum(passed / total for _, passed, total in max_heap)
        return total_ratio / len(classes)
solution = Solution()
print(solution.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
print(solution.maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))
