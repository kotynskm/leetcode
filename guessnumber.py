""" We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked. """

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # guess which number was picked
        # if guess is higher, lower, or equal
        # calculate the middle and guess there, adjust pointers if higher or lower, return if equal
        l,r = 1, n
        
        while l <= r:
            mid = (l + r)//2
            
            if guess(mid) == 0:
                return mid
            
            if guess(mid) == -1:
                r = mid - 1
            
            if guess(mid) == 1:
                l = mid + 1