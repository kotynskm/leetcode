"""Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur."""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # we want to count consecutive groups of 1s and 0s
        # so we can use a q and when the next number does not match the last item in the queue, we pop from the queue and append the new number to the front the queue
        # use a while loop to account for many leading characters
        # when character is equal to one at the end, but not the one at beginning
        q = deque()
        count = 0

        for num in s:
            while q and num == q[-1] and q[0] != num:
                q.pop()
            
            if q and num != q[-1]:
                q.pop()
                count += 1
            
            q.appendleft(num)

        return count