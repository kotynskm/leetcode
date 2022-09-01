""" Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in 

the range [1, n] that do not appear in nums."""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # make a hash table of nums in range of 1, to n
        num_range = {}
        
        for i in range(1, len(nums) + 1):
            num_range[i] = True
        
        # loop over nums and remove the nums from num_range that are present in nums
        for num in nums:
            if num in num_range:
                del num_range[num]
                
        return num_range