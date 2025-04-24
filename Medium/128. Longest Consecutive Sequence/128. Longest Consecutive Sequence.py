'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)  # Create the set of nums
        max_seq = 0

        for num in nums_set:

            # Check if it is the start of a sequence
            # Utilize Hashmap O(1) lookups
            if (num - 1) not in nums_set:
                curr = num
                curr_seq_length = 1

                while (curr + 1) in nums_set:
                    curr += 1
                    curr_seq_length += 1

                max_seq = max(max_seq, curr_seq_length)

        return max_seq

def main():
    solution = Solution()

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),                   # 1, 2, 3, 4
        ([0,3,7,2,5,8,4,6,0,1], 9),                    # 0 through 8
        ([1, 2, 0, 1], 3),                             # 0, 1, 2
        ([9,1,-3,2,4,8,3,-1,6,-2,-4,7], 7),            # -4 to 2
        ([], 0),                                       # Empty input
        ([1], 1),                                      # Single element
        ([1,2,0,1], 3),                                # Repeats included
        ([-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1], 1),        # Only length-1 sequences
        ([10, 5, 12, 3, 55, 30, 2, 4, 11, 6], 5),       # 2,3,4,5,6
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.longestConsecutive(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status} — Expected {expected}, Got {result}")

if __name__ == "__main__":
    main()

'''
Time Complexity - O(n) - Given we create a set which is a O(n) operation and iterating over that set is a < O(n) operation 
Space Complexity - O(n) - worst case is that all of the input nums are unique. 
'''
