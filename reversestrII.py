""" Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space. """

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the entire str first with helper function
        def reverse(s, left, right):
            while left <= right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1

            return s
        
        reverse_str = reverse(s, 0, len(s) -1)

        # reverse each word in the str
        n = len(reverse_str)
        start, end = 0,0 

        # while start is less than total length
        while start < n:
            # while end is less than total length and is not a space, advance it
            while end < n and reverse_str[end] != " ":
                end += 1

            # pass start and end into reverse to reverse that word
            reverse(reverse_str, start, end - 1)

            # advance start and end pointers to the next word
            start = end + 1
            end += 1