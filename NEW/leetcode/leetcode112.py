# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if node is None:
                return False
            elif not node.left and not node.right:
                return target == node.val
            else:
                return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
        
        return dfs(root, targetSum)