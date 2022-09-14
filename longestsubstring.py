""" Given a string s, find the length of the longest substring without repeating characters. """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set of characters
        char_set = set()
        # result variable
        result = 0
        # left pointer
        l = 0
        
        # loop with r pointer
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)
        return result