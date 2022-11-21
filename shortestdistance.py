""" Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list."""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # loop over words and keep track of the indices of each word
        # when we see the same word we can update the index and check if the distance between the updated indices is less than what is currently stored

        index1, index2 = -1,-1
        shortest_dist = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            
            if index1 != -1 and index2 != -1:
                distance = abs(index1 - index2)
                shortest_dist = min(distance, shortest_dist)

        return shortest_dist
