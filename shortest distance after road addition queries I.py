from typing import List
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1)) 
        def dijkstra():
            dist = [float('inf')] * n
            dist[0] = 0
            min_heap = [(0, 0)]  
            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d > dist[u]:
                    continue
                
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            
            return dist[n - 1]
        
        result = []
        for u, v in queries:
            graph[u].append((v, 1)) 
            shortest_path = dijkstra()
            result.append(shortest_path)
        
        return result
