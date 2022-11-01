""" Given the root of a binary tree, return the postorder traversal of its nodes' values. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post order is visit left, then right, then node
        res = []
        
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)
            res.append(node.val)
        
            return res
        
        return dfs(root)