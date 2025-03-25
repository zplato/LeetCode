from collections import OrderedDict


class LRUCache:

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    #
    # Initial solution - using regular dictionary simulating an ordered dict
    #
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.LRU_key = -1
    #     self.cache = {}

    # def get(self, key: int) -> int:
    #     # Key Exists, so update last recently used
    #     if key in self.cache:
    #         value = self.cache.pop(key)
    #         self.cache[key] = value # reinsert to move this to the front
    #         self.LRU_key = list(self.cache.keys())[0]
    #         return self.cache[key]
    #     return -1

    # def put(self, key: int, value: int) -> None:

    #     #print(f"Method: Put, LRU_key: {self.LRU_key}, self.cache: {self.cache}")
    #     # If key does not exist, then insert it
    #     if self.cache.get(key, -1) == -1 and len(self.cache) < self.capacity:
    #         self.cache[key] = value
    #     # Key exists
    #     elif self.cache.get(key, -1) != -1:
    #         self.cache.pop(key)
    #         self.cache[key] = value
    #     elif len(self.cache) >= self.capacity:
    #         # remove the last recently used item from the cache
    #         self.cache.pop(self.LRU_key)
    #         self.cache[key] = value
    #     else:
    #         # We have room, length of the cache is less than the capacity
    #         self.cache.pop(key)
    #         self.cache[key] = value

    #     # Update LRU
    #     self.LRU_key = list(self.cache.keys())[0]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.setdefault(key, self.cache.pop(key))  # Set to last item in dict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Its already in there, so just update the value
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            # its not in there, so add it and check if we need to remove the oldest one
        else:
            self.cache[key] = value
            if (len(self.cache) > self.capacity):
                self.cache.popitem(last=False)  # Pop the first (oldest) item in the ordered dict


def main():
    print("Running LRU Cache Test Cases:\n")

    def test_case(result, expected, description=""):
        status = "PASS" if result == expected else "FAIL"
        print(f"{description} Result: {result} | Expected: {expected} | {status}")

    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    test_case(lru.get(1), 1, "Get(1):")

    lru.put(3, 3)  # Evicts key 2
    test_case(lru.get(2), -1, "Get(2) after evicting 2:")

    lru.put(4, 4)  # Evicts key 1
    test_case(lru.get(1), -1, "Get(1) after evicting 1:")
    test_case(lru.get(3), 3, "Get(3):")
    test_case(lru.get(4), 4, "Get(4):")

    # Additional custom tests:
    lru.put(5, 5)  # Evicts key 3
    test_case(lru.get(3), -1, "Get(3) after evicting 3:")
    test_case(lru.get(4), 4, "Get(4) should still exist:")
    test_case(lru.get(5), 5, "Get(5):")

if __name__ == "__main__":
    main()



"""
Approach:
---------
- This implementation of an LRU (Least Recently Used) cache uses Python's built-in OrderedDict, 
  which maintains the insertion order of keys.
- On `get(key)`:
    - If the key exists, move it to the end of the OrderedDict to mark it as recently used.
    - Return the associated value.
    - If it doesn't exist, return -1.
- On `put(key, value)`:
    - If the key exists, move it to the end and update its value.
    - If the key does not exist, insert it at the end.
    - If inserting the new key exceeds the cache's capacity, remove the oldest (least recently used) item from the beginning.

Why OrderedDict:
----------------
- `OrderedDict.move_to_end()` allows O(1) operations to reorder keys.
- `OrderedDict.popitem(last=False)` removes the oldest inserted item in O(1) time.

Time Complexity:
----------------
- `get()` and `put()` operations are O(1).

Space Complexity:
-----------------
- O(capacity), as the cache will hold up to 'capacity' elements.

This solution meets both efficiency and clarity standards for an LRU cache.
"""