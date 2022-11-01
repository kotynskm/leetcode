""" Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. """

        # make a helper function that takes in the l and r
        # if l > r return None
        # calc the mid and set that as root TreeNode
        # pass the left side back into helper with pointers updated
        # pass the right side back into helper with pointers updated
        # call the helper with l and r, which are 0 and len(nums) - 1
        
        def helper(l,r):
            if l > r:
                return None
            
            mid = (l + r)//2
            root = TreeNode(nums[mid])
            
            # recursive calls
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
            
        return helper(0, len(nums) -1)
        