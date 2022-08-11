""" Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as

the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself). ”"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # set current to the root node
        curr = root
        
        # loop while current is not null
        while curr:
            # check if p and q are greater than, or less than the current node
            if p.val < curr.val and q.val < curr.val:
                # update current node to the left node
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # update current node to the right node
                curr = curr.right
            else:
                # there must have been a split to the left side and right side,
                # return the current node before the split occured
                return curr