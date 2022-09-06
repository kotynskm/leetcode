""" Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if no left nodes, return depth of the right
        if root.left is None:
            return 1 + self.minDepth(root.right)
        # if no right nodes, return depth of the left
        if root.right is None:
            return 1 + self.minDepth(root.left)
        # if both have nodes, return the min depth between the two
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))