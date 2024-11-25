from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = '123450' 
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        queue = deque([(start, start.index('0'), 0)]) 
        visited = set([start])

        while queue:
            state, zero_pos, steps = queue.popleft()
            if state == target:
                return steps
            for neighbor in neighbors[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, neighbor, steps + 1))
        return -1    