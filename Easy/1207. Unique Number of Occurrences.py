from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Iterate through the list and get a freq map of occurrences, where key = num, value = freq
        # Then, check if there exists any two values the same, if not, return True, else False

        freq_map = {}

        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        return len(set(freq_map.values())) == len(freq_map.values())

    """
    Time Complexity O(n) - iterate over the input n
    Space Complexity O(n) - store freq_map of at most length n
    """