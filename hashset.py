""" Design a HashSet without using any built-in hash table libraries. """

class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hash_set)):
            if self.hash_set[i] == key:
                self.hash_set.pop(i)
                break

    def contains(self, key: int) -> bool:
        return key in self.hash_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)