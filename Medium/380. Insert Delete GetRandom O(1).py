"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
    Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Constraints:
    -231 <= val <= 231 - 1
    At most 2 * 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.
"""


import random


class RandomizedSet:

    # Approach - Given O(1) lookup time, we know that set operations have O(1) naturally.
    # This is a tricky problem though, because we cannot utilize getRandom naturally with only a set. Converting to a list is O(n)
    # So... Under the hood we need to utilize a list, and then a dictionary {val : index} to support O(1) lookups

    def __init__(self):
        # self.randomized_set = set()
        self.support_dict = {}  # key = num, value = index - since this is a set, there are only unique nums
        self.support_list = []

    def insert(self, val: int) -> bool:

        # Check if it already exists in set, if so then Return False as we didn't add it
        if val in self.support_dict.keys():
            return False

        # It doesn't exist, so add it and return True
        else:

            # Original Approach using a set
            # self.randomized_set.add(val)

            # Approach with list + dict
            self.support_list.append(val)
            self.support_dict[val] = len(
                self.support_list) - 1  # value : index - Since this is a set, we can utiilze value for key
            return True

    def remove(self, val: int) -> bool:
        if val in self.support_dict.keys():

            # Original Approach using a set
            # self.randomized_set.discard(val)

            # Approach with list + dict
            removal_idx = self.support_dict.get(val)  # Use this to support O(1) operations with list
            # self.support_list.remove(removal_idx) # This removes the specified value, not at the specified index
            # del self.support_list[removal_idx] - this is not O(1) for lists, and shifts values in the list to the left which
            #   invalidates the indices of the dict

            # Tricky tricky - need to actually make a hard swap of elements we want to delete and put it to the end
            # First check if its not already at the end - if it is at the end then we can skip the swap and just pop it
            if self.support_list[-1] != self.support_list[removal_idx]:
                temp = self.support_list[-1]  # store value at last index temporarily
                self.support_list[-1] = self.support_list[
                    removal_idx]  # Overwrite value at last index with the value we want to delete
                self.support_list[
                    removal_idx] = temp  # Over write the value at removal index with the value we are keeping
                self.support_dict[
                    temp] = removal_idx  # Update the dict with the value : index we didn't delete but swapped

            self.support_list.pop()  # Remove that last element now
            del self.support_dict[val]  # This is O(1) for dicts

            return True

            # Doesn't even exist in set
        else:
            return False

    def getRandom(self) -> int:

        # Original Approach with set
        # Convert to a list, then utilize random.choice to return a random num from the list
        # random_num = random.choice(list(self.randomized_set)) # This is O(n) and doesn't qualify for O(1)

        # Approach with list + dict
        random_num = random.choice(self.support_list)  # For O(1) we utilize a list
        # random_num_idx = self.support_dict.get(random_num) - If we wanted to get the index of the number, we can do it this way
        return random_num

    # Your RandomizedSet object will be instantiated and called as such:


# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
Time Complexity  - O(1): Utilizes Dict for all method O(1) lookups 
Space Complexity - O(n): Utilzing a list and a dict of length n, so 2*n simplifies to O(n) 
"""
