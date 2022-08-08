# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        def dfs(node, result):
            if node:
                dfs(node.left, result)
                result.append(node.val)
                dfs(node.right, result)
        stack = []
        dfs(root, stack)
        return stack