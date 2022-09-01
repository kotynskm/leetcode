""" Given a characters array letters that is sorted in non-decreasing order and a character target, 

return the smallest character in the array that is larger than target.

Note that the letters wrap around. """

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        
        # check if target is less than lowest letter, or greater than greatest letter, if so then return the first letter in letters
        if target < letters[l] or target >= letters[r]:
            return letters[l]
        
        # perform binary search
        while l <= r:
            mid = (l + r)//2
            
            if target < letters[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
                
        return letters[l]