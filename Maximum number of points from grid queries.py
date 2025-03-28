import heapq

class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        results = []
        visited = [[False] * n for _ in range(m)]

        # Min-heap to process cells in increasing order of value
        heap = [(grid[0][0], 0, 0)]  # (value, x, y)
        visited[0][0] = True

        # Precompute points for every possible threshold
        points = [0] * (10**6 + 1)
        points_count = 0

        for value in range(1, 10**6 + 1):
            # Process all cells with value less than the current threshold
            while heap and heap[0][0] < value:
                _, x, y = heapq.heappop(heap)
                points_count += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(heap, (grid[nx][ny], nx, ny))
            points[value] = points_count

        # Compute the results for each query
        for query in queries:
            results.append(points[query])

        return results
