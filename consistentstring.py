""" You are given a string allowed consisting of distinct characters and an array of strings words. 

A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words. """

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        # loop through each word, get each character - if not in allowed, add to count and break
        # to move on to the next word
        for word in words:
            for c in word:
                if c not in allowed:
                    count += 1
                    break
        # subtract all invalid words from the length and we will have count of consistent words
        return len(words) - count