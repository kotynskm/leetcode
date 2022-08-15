""" Given two strings ransomNote and magazine, return true if ransomNote can be constructed
 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote. """

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create count dicts of the letters
        countM = {}
             
        # create keys,values for magazine dict
        for i in range(len(magazine)):
            countM[magazine[i]] = 1 + countM.get(magazine[i], 0)
            
        # loop through ransom note and compare to magazine dict
        for letter in ransomNote:
            # if the letter is in magazine, check the count - if it's > 0 subtract from the current count
            if letter in countM and countM[letter] > 0:
                countM[letter] -= 1
            # the count of letters in ransom is greater than available from magazine
            else:
                return False
            
        return True
            