""" Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. """

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count_map = {}
        # creates a freq array, with arrays at each index all the way to the length of the input
        freq = [[] for i in range(len(nums) + 1)]
        
        # populate hash table with nums and counts
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)
            
        # populate freq table
        for number, count in count_map.items():
            freq[count].append(number)
            
        # loop over freq table starting from the back, because that's the highest count
        for i in range(len(freq) - 1, 0, -1):
            # there may be multiple nums at that frequency, so must loop over them
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

# solution using a heap
from heapq import *


def find_k_largest_numbers(nums, k):
  minHeap = []

  # insert first k elements
  for i in range(k):
    heappush(minHeap, nums[i])

  # loop rest of elements and compare to what is in heap
  for j in range(k, len(nums)):
    if nums[j] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[j])

  return minHeap