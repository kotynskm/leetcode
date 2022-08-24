""" Given a string s which consists of lowercase or uppercase letters, return the length of the 

longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here. """

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # make a hash table to count occurrences of the letter
        letter_counts = {}
        result = 0
        
        # loop and populate the hash table
        for char in s:
            letter_counts[char] = 1 + letter_counts.get(char, 0)
            
        # loop values and add to result
        for val in letter_counts.values():
            result += val//2 * 2
            if result % 2 == 0 and val % 2 == 1:
                result += 1
        return result