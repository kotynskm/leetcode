""" Given the root of a binary tree and an integer targetSum, return true if the tree has a 

root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case - we've traversed all nodes and never hit our true condition
        if not root:
            return False
        # if we are on a leaf node, and sum - val is zero, this is our true condition
        if not root.right and not root.left and targetSum - root.val == 0:
            return True
        
        # recurse
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)