""" Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward. """

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l,r = 0, len(word) - 1
            
            while l < r:
                if word[l] != word[r]:
                    break
                
                l += 1
                r -= 1
            if l >= r:
                return word
            
        return ""