""" Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        if not root:
            return []
        
        def helper(node, target, prevPathsVisited):
            prevPathsVisited.append(node.val)
            
            # leaf node and correct path
            if not node.left and not node.right and node.val == target:
                res.append(prevPathsVisited)
            
            if node.left:
                helper(node.left, target - node.val, prevPathsVisited.copy())
                
            if node.right:
                helper(node.right, target - node.val, prevPathsVisited.copy())
                
        helper(root, targetSum, [])
        return res