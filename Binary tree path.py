from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)
        
        result = []
        dfs(root, "")
        return result
