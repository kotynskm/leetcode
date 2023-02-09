""" Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        num_set = set()

        for num in arr:
            hash[num] = hash.get(num, 0) + 1

        for value in hash.values():
            num_set.add(value)

        return len(num_set) == len(hash)

# We can optimize by adding values if not already in the set - we can return early if we see a repeat number
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        num_set = set()

        for num in arr:
            hash[num] = hash.get(num, 0) + 1

        for value in hash.values():
            if value not in num_set:
                num_set.add(value)
            else:
                return False

        return True
        