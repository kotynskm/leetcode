""" Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order. """

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_table = {}
        result = []
        words.sort()
        
        # create based on length of words
        freq = [ [] for i in range(len(words) + 1) ]
        
        # populate word table
        for word in words:
            word_table[word] = 1 + word_table.get(word, 0)
            
        
            
        for word, count in word_table.items():
            freq[count].append(word)
            
        # loop backwards through the freq array, looping each array
        for i in range(len(freq) - 1, 0, -1):
            for word in freq[i]:
                result.append(word)
                if len(result) == k:
                    return result