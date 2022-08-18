""" Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. """

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums) - 1
        
        result = []
        
        squareStart = 0
        squareEnd = 0
        
        while l <= r:
            # calc the square of each
            squareStart = nums[l] * nums[l]
            squareEnd = nums[r] * nums[r]
            
            # check which is bigger
            if squareStart > squareEnd:
                result.append(squareStart)
                l += 1
            else:
                result.append(squareEnd)
                r -= 1
                
        return result[::-1]