'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        '''
            Approach - Utilize hash_map to detect duplicates and store indicies
                where key = num, value = [i]
                If duplicate is found, then execute abs(i - j) <= k
                return True if equality is satisfied
                else keep looking
                if iteration is complete, then return False as we found
        '''
        # num_map = {}

        # for i, num in enumerate(nums):

        #     # If duplicate is found
        #     if num_map.get(num, []):
        #         for j in num_map[num]:
        #             if abs(i - j) <= k:
        #                 return True

        #     # If no duplicate is found, then store the num
        #     num_map[num] =  num_map.get(num, []) + [i]

        '''
        Appraoch 2 - Utilize hashmap with sliding window, where 
            Key = num and value = Index of num (window that only looks at last)
            This is because any earlier index will be further away,
            so only store the latest index. 
        '''
        num_map = {}

        for i, num in enumerate(nums):

            # Check if its a duplicate
            if num in num_map and abs(i - num_map[num]) <= k:
                return True

                # create or update value in map
            num_map[num] = i

        return False

def main():
    solution = Solution()

    test_cases = [
        # Format: (nums, k, expected_result)
        ([1, 2, 3, 1], 3, True),          # Duplicate 1 within distance 3
        ([1, 0, 1, 1], 1, True),          # Duplicate 1 at distance 1
        ([1, 2, 3, 1, 2, 3], 2, False),   # Duplicates exist but all are > k apart
        ([99, 99], 2, True),              # Immediate duplicate
        ([1, 2, 3, 4, 5], 10, False),     # No duplicates
        ([1, 2, 3, 4, 1], 3, False),      # Duplicate but too far apart
        ([1, 2, 1], 2, True),             # Duplicate within range
        ([], 1, False),                   # Edge case: empty list
        ([1], 0, False),                  # Single element, no room for duplicate
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.containsNearbyDuplicate(nums, k)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status} — Expected {expected}, Got {result}")

if __name__ == "__main__":
    main()

'''
Time Complexity - O(n): Iterate over all numbers once 
Space Complexity - O(n): store all n nums in a num_map, worst case no duplicates so O(n) 
'''