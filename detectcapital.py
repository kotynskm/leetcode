""" We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        
        # loop word and count capitals
        for i in range(len(word)):
            if word[i].isupper():
                count += 1
                
        # all letters are capital       
        if count == len(word):
            return True
            
        # first letter is capital
        if count == 1 and word[0].isupper():
            return True
        
        # if all lower case
        if count == 0:
            return True
        
        # all other cases are false
        return False