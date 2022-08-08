# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 매우 비효율적인데 정답은 맞추긴했음...
import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target, res):
            if node is None:
                return []
            elif not node.left and not node.right:
                is_target = target == node.val
                if is_target:
                    res.append(node.val)
                    result.append(res)
            else:
                res.append(node.val)
                if node.left:
                    res2 = copy.deepcopy(res)
                    dfs(node.left, target - node.val, res2)
                if node.right:
                    res2 = copy.deepcopy(res)
                    dfs(node.right, target - node.val, res2)
        result = []
        dfs(root, targetSum, [])
        return result