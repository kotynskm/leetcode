""" Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both p and q are None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # iterative solution with BFS and queue
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS with queue
        que = [(p, q)]
        
        while que:
            # pop nodes
            node1, node2 = que.pop(0)
            # if both are None
            if not node1 and not node2:
                return True
            # if only one is None
            if not node1 or not node2:
                return False
            # if the values are not equal
            if node1.val != node2.val:
                return False
            # append left and right nodes
            que.append((node1.left, node2.left))
            que.append((node1.right, node2.right))  