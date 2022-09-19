""" Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 

return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space. """

# this solution uses O(n) space with the use of the hash table
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # make a hash table
        num_count = {}
        res = []
        
        # populate the hash table
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
            
        # return an array of nums with a count of 2
        for number in num_count:
            if num_count[number] == 2:
                res.append(number)
        
        return res
        
# O(n) no extra space solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # loop nums and calc index by taking abs(num) - 1
        for num in nums:
            index = abs(num) - 1
        # if num at index is already negative, then we already saw that number
            if nums[index] < 0:
                res.append(index + 1)
        # turn the number negative to indicate we saw the value
            else:
                nums[index] = nums[index] * -1
        
        return res

