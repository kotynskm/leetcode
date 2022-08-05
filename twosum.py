""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """

def twoSum(nums, target): 
    # loop and get first num
    for i in range(0, len(nums)):
    # loop and get second num
        for j in range(i+1, len(nums)):
            # does sum of num[i] and num[j] == target? if so, return i and j  
            if nums[i] + nums[j] == target:
                return i,j

# solution with enumerate

def twoSum(nums, target):
    # create a hash table to store nums in array
    num_dict = {}
        
    # loop with enumerate
    for i,num in enumerate(nums):
        # calc num needed
        num_needed = target - num
        if num_needed in num_dict:
            return [i, nums.index(num_needed)]
        else:
            num_dict[num] = True
    return []