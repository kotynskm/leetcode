""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string. """

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # loop for length of first string in the list
        for i in range(len(strs[0])):
            # loop over each word in strs
            for word in strs:
                # if character at i from the current word does not equal the first words character at i, or i is the same as the length of the word (so we don't go out of bounds)
                if i == len(word) or word[i] != strs[0][i]:
                    return res
            # if they are the same then we add the character at i to the result
            res += strs[0][i]
            
        return res