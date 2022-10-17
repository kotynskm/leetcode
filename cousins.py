""" Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding

 to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        
        # deque with a tuple of the root, and it's parent value - initialized with None because the root does not have a parent
        q = deque()
        q.append((root, None))
        depth = 0
        d = {}
        
        while q:
            depth += 1
            for i in range(len(q)):
                node, node_parent_value = q.popleft()
                
                if node.left:
                    # node.val is the parent value
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))
        
                # put dictionary values
                d[node.val] = (depth, node_parent_value)
        print(d)
        if d[x][0] == d[y][0] and d[x][1] != d[y][1]:
            return True
        
        return False
        