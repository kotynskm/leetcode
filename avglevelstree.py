""" Given the root of a binary tree, return the average value of the nodes on each level 

in the form of an array. Answers within 10-5 of the actual answer will be accepted. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque([root])
        result = []
        
        # add the first node to the q
        q.append(root)
        
        # while q is not empty, loop
        while q:
            # get length of q and reset sum
            length = len(q)
            sum = 0
            # calc sum in range length of q
            for i in range(length):
                # pop the left node and add val to sum
                current_node = q.popleft()
                sum += current_node.val
                # check for children and add them to q
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                
            avg = float(sum)/float(length)
            result.append(avg)
            
            
        return result