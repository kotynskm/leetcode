""" Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
            
            return values
        
        value_list = dfs(root)
        
        ans = curr_node = TreeNode(None)
        
        for i in range(len(value_list)):
            curr_node.right = TreeNode(value_list[i])
            curr_node = curr_node.right
        
        return ans.right