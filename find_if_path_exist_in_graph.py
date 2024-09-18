from collections import deque, defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if source == destination:
            return True
        queue = deque([source])
        visited = set([source])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
solution = Solution()
n1, edges1, source1, destination1 = 3, [[0,1],[1,2],[2,0]], 0, 2
print(solution.validPath(n1, edges1, source1, destination1))
n2, edges2, source2, destination2 = 6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5
print(solution.validPath(n2, edges2, source2, destination2))