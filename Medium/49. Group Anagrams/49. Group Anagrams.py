'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Anagrams are rearranged words -
        # or in otherwords, they have the same letters in diff combinations

        # Approach - Utilize a Hashmap where:
        # Key = sorted word, Value = List of words that are anamgrams
        # Return map.values()

        anagrams_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            # Check if it exists already
            if sorted_word in anagrams_map:
                anagrams_map[sorted_word].append(word)

            # If it doesn't exist then add it
            else:
                anagrams_map[sorted_word] = [word]

        return list(anagrams_map.values())

def main():
    solution = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),  # Edge case: empty string
        (["a"], [["a"]]),  # Single character
        (["abc", "cba", "bac", "bca", "cab", "acb"], [["abc", "cba", "bac", "bca", "cab", "acb"]]),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),  # No anagrams
        (["a", "b", "a"], [["a", "a"], ["b"]]),  # Repeated simple chars
    ]

    for i, (input_list, expected_groups) in enumerate(test_cases, 1):
        output = solution.groupAnagrams(input_list)

        # Convert inner lists to sets for unordered comparison
        output_sets = [set(group) for group in output]
        expected_sets = [set(group) for group in expected_groups]

        # Since order of groups doesn't matter, sort lists of sets before comparison
        result = sorted(output_sets) == sorted(expected_sets)
        status = "PASSED" if result else "FAILED"
        print(f"Test case {i}: {status}")

if __name__ == "__main__":
    main()

''' 
Time Complexity - O(n * (k log k)): 
- n = number of strings
- k = maximum length of a string
- Each string is sorted (O(k log k)) and inserted into a hashmap

Space Complexity - O(n * k): Creating a hashmap with n values to store and keys of length k 
'''