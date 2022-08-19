""" Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory. """

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use two pointers
        ind1, ind2 = 0, len(s) -1
        
        # loop while ind1 <= ind2
        while ind1 <= ind2:
            # store letter at ind1, then swap the letters and move indexes
            tmp = s[ind1]
            s[ind1] = s[ind2]
            s[ind2] = tmp
            ind1+=1
            ind2-=1
        
        return s