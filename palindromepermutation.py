""" Given a string s, return true if a permutation of the string could form a 
palindrome
 and false otherwise. """

 class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # a permutation is a rearrangment of the letters
        # a palindrome must have all even counts of letters and at most 1 odd count (the possible middle letter)
        # make a hash table of the letter counts
        # loop hash table and check counts, if the count is odd, if it is increase odds count
        # if odds count ever gets above 1, then it's not possible to create a palindrome
        hash = {}
        odds_count = 0
        s_lst = list(s)

        for letter in s_lst:
            hash[letter] = hash.get(letter, 0) + 1

        for letter in hash:
            if hash[letter] % 2 != 0:
                odds_count += 1

                if odds_count > 1:
                    return False
        
        return True
