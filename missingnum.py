""" Given an array nums containing n distinct numbers in the range [0, n], 

return the only number in the range that is missing from the array. """

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_table = {}
        
        for i in range(len(nums) + 1):
            nums_table[i] = True

        for num in nums_table:
            if num not in nums:
                return num