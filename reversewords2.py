""" Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 

The returned string should only have a single space separating the words. Do not include any extra spaces."""

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_str = ""
        # trim the extra whitespace off string
        s.strip()
        # split the string into an array of words by splitting space
        words_list = s.split()

        # iterate over each word and reverse the order
        for i in range(len(words_list)-1,-1,-1):
            if i == 0:
                reversed_str += words_list[i]
            else:
                reversed_str += words_list[i] + " "
            
        return reversed_str