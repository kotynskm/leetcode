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

# solution using O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        
        # calc the sum expected and the sum actual
        sumExp = length * (length + 1)//2
        sumActual = sum(nums)
        
        return sumExp - sumActual