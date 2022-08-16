""" Given a sorted array of distinct integers and a target value, return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity. """

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # set l and r pointer
        l, r = 0, len(nums) - 1
        
        # loop while l <= r
        while l <= r:
            # calc the mid
            mid = (l + r)//2
            
            # compare target to value at mid index, update mid
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
                
            if target < nums[mid]:
                r = mid - 1  
                
        return l
                
                
        