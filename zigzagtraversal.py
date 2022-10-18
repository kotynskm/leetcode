""" Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between). """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use flag to alternate which side to append
        alternate = True
        result = []
        q = deque([root])
        
        if not root:
            return None
        
        
        while q:
            lst = deque()
            for i in range(len(q)):
                node = q.popleft()
                
                if alternate:
                    lst.append(node.val)
                else:
                    lst.appendleft(node.val)
                
                # check and append children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            result.append(lst)    
            # switch the flag
            alternate = not alternate
         
        return result