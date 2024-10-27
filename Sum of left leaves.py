from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None
        if root is None:
            return 0
        left_sum = 0
        if root.left and is_leaf(root.left):
            left_sum += root.left.val
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)
        
        return left_sum   