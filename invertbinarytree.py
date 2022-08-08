""" Given the root of a binary tree, invert the tree, and return its root. """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use recursion
        # base case
        if not root:
            return None
        
        # else swap root.left and root.right
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # pass root.right and root.left back into function
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        # return the root
        return root