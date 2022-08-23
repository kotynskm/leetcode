""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 

using all the original letters exactly once. """

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hashmap
        store = defaultdict(list)
        
        # create a count list for each word with 26 zeros
        for word in strs:
            count = [0] * 26
            # loop each char in the word and calc index of value and increment the count
            for char in word:
                count[ord(char) - ord('a')] += 1 
                
            # add the count as a tuple key, with the word as a value
            store[tuple(count)].append(word)
           
        # return the values
        return store.values()