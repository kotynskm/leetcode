""" Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1. """

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # make a hash table and fill with numbers that are only even
        # then loop hash and compare counts

        hash = {}

        for num in nums:
            if num % 2 == 0:
                hash[num] = hash.get(num, 0) + 1
        
        current_count = 0
        res = -1

        for key in hash:
            if hash[key] > current_count:
                current_count = hash[key]
                res = key
            if hash[key] == current_count:
                if key < res:
                    res = key

        return res