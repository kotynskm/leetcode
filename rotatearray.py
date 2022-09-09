""" Given an array, rotate the array to the right by k steps, where k is non-negative. """

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        
        for i, num in enumerate(nums):
            new_index = i + k
            
            if new_index >= len(nums):
                new_index = new_index % len(nums)
                result.insert(new_index, num)
            else:
                result.insert(new_index, num)
                
        for i in range(len(nums)):
            nums[i] = result[i]