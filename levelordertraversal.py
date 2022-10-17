""" Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level). """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root])
        
        if root == None:
            return None
        
        while q:
            lst = []
            for i in range(len(q)):
                current = q.popleft()
                lst.append(current.val)
                
                # check and add children nodes
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            result.append(lst)
        
        return result
        