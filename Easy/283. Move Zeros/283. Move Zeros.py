"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Approach 1 -  Utilize a two pointer approach
        #               First pointer is the loop iterator
        #               Second pointer is the write pointer for non-zero writes
        #               After the loop is finished, fill in the remainder of the
        #               list with 0's after the write pointer

        i = 0  # read pointer
        j = 0  # write pointer
        while i < len(nums):
            # If current number is non-zero, write it to nums[j]
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1

            # At this point, everything after j is zero because we shifted all non-zero
        # numbers left
        while j < len(nums):
            nums[j] = 0
            j += 1

def main():
    sol = Solution()

    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([0], [0]),
        ([1], [1]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        input_copy = nums.copy()
        sol.moveZeroes(nums)
        print(f"  Input:    {input_copy}")
        print(f"  Output:   {nums}")
        print(f"  Expected: {expected}")
        print(f"  Pass:     {nums == expected}\n")


if __name__ == "__main__":
    main()


"""
Time Complexity: O(n)
    - One pass to shift non-zeroes
    - One pass to fill in zeroes

Space Complexity: O(1)
    - In-place modification using constant extra space
"""