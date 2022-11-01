""" Given the root of a binary tree, return the preorder traversal of its nodes' values. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder is as you visit each node record its value
        res = []
        
        def dfs(node):
            if not node:
                return None
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
            return res
        
        return dfs(root)