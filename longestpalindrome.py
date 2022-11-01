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

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # make a count d of letter counts
        # loop count dict
        # if count is even, add it to total count
        # if number is odd add value - 1 ( we leave the odd 1 out) and increment count of odd numbers
        # if odd count > 1 then we add an additional 1 for the middle char of the palindrome
        
        d = {}
        longest = 0
        countOdds = 0
        
        for char in s:
            d[char] = 1 + d.get(char, 0)
            
        for char in d:
            if d[char] % 2 == 0:
                longest += d[char]
            else:
                longest += d[char] - 1
                countOdds += 1
            
        if countOdds:
            longest += 1
                
        return longest