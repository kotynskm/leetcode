""" Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
      
        def dfs(root):
            nonlocal balanced
            if not root:
                return True
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
                balanced = False
                
            return max(left, right) + 1
            
        
        dfs(root)
        return balanced