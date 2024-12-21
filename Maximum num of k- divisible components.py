from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = [False] * n
        result = 0

        def dfs(node: int) -> int:
            nonlocal result
            visited[node] = True
            current_sum = values[node]
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    subtree_sum = dfs(neighbor)
                    if subtree_sum % k == 0:
                        result += 1
                    else:
                        current_sum += subtree_sum

            return current_sum
        total_sum = dfs(0)
        if total_sum % k == 0:
            result += 1

        return result
