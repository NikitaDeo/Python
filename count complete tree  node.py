from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        def getDepth(node):
            depth = 0
            while node.left:
                depth += 1
                node = node.left
            return depth
        
        depth = getDepth(root)
        
        
        if depth == 0:
            return 1
            
        left, right = 0, (1 << depth) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            if self.exists(mid, depth, root): 

                left = mid + 1
            else:
                right = mid - 1

        return (1 << depth) - 1 + left  


    def exists(self, index: int, depth: int, node: Optional[TreeNode]) -> bool:
        """Check if the index-th node exists in the last level."""
        left, right = 0, (1 << depth) - 1 
        for _ in range(depth):
            mid = (left + right) // 2
            if index <= mid: 
                node = node.left
                right = mid
            else: 
                node = node.right
                left = mid + 1
            if not node: 
                return False
        return True 