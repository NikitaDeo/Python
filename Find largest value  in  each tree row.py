from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        largest_values = []
        queue = [root]

        while queue:
            level_max = float('-inf')
            next_queue = []
            for node in queue:
                level_max = max(level_max, node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            largest_values.append(level_max)
            queue = next_queue

        return largest_values
