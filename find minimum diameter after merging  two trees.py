from collections import deque
from typing import List

class Solution:
    def treeDiameterAndMaxDepth(self, edges: List[List[int]]) -> (int, int):
        def bfs(node):
            visited = [-1] * len(adj)
            visited[node] = 0
            q = deque([node])
            farthest_node = node

            while q:
                curr = q.popleft()
                for neighbor in adj[curr]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[curr] + 1
                        q.append(neighbor)
                        farthest_node = neighbor

            return farthest_node, max(visited)
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        farthest_node, _ = bfs(0)
        _, diameter = bfs(farthest_node)
        _, max_depth = bfs(0)

        return diameter, max_depth

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        diameter1, maxDepth1 = self.treeDiameterAndMaxDepth(edges1)
        diameter2, maxDepth2 = self.treeDiameterAndMaxDepth(edges2)
        return max(diameter1, diameter2, maxDepth1 + maxDepth2 + 1)
solution = Solution()
print(solution.minimumDiameterAfterMerge([[0,1],[0,2],[0,3]], [[0,1]]))  
print(solution.minimumDiameterAfterMerge(
    [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], 
    [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
)) 
