class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root, queries):
        def calculate_heights(node):
            if not node:
                return -1 
            left_height = calculate_heights(node.left)
            right_height = calculate_heights(node.right)
            height[node.val] = 1 + max(left_height, right_height)
            return height[node.val]
        def compute_remaining_height(node, exclude_val):
            if not node or node.val == exclude_val:
                return -1
            left_height = compute_remaining_height(node.left, exclude_val)
            right_height = compute_remaining_height(node.right, exclude_val)
            return 1 + max(left_height, right_height)
        height = {}
        calculate_heights(root)
        result = []
        for query in queries:
            remaining_height = compute_remaining_height(root, query)
            result.append(remaining_height)
        
        return result