'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

            # Approach 1 - since this is a known problem, the solution here is to first find the real k since it repeats
        k %= len(nums)  # Gives the remainder - what we actually need to rotate by

        nums.reverse()  # Reverse in place

        # Now we reverse the substrings slice of characters and add the two together to create the return
        # nums = nums[:k][::-1] + nums[k:][::-1] # The issue here is that the slice [::-1] returns a new string nums and doesn't modify the original

        # reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # reverse elements after k
        nums[k:] = reversed(nums[k:])

        # Debugging Help
        # print(nums)

        # Not necessary as we reversed in place and python doesn't require a return
        return

# Space Time Complexity:
# Time - O(n) - since we utilize .reverse() which is O(n) and additionally utilize slicing which equates to O(n)
# Space - O(1) - Modify in place

def run_test(test_id: int, nums: List[int], k: int, expected: List[int]):
    sol = Solution()
    input_copy = nums.copy()  # Keep original for printing
    sol.rotate(nums, k)
    if nums == expected:
        print(f"Test {test_id}: PASS")
    else:
        print(f"Test {test_id}: FAIL")
        print(f"  Input:    {input_copy}, k = {k}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {nums}")


def main():
    test_cases = [
        # Format: (test_id, nums, k, expected)
        (1, [1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        (2, [-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        (3, [1, 2], 3, [2, 1]),  # k > len(nums)
        (4, [1], 0, [1]),        # k = 0
        (5, [], 4, []),          # empty list
        (6, [1, 2, 3], 3, [1, 2, 3]),  # k == len(nums)
        (7, [1, 2, 3, 4], 1, [4, 1, 2, 3])
    ]

    for test_id, nums, k, expected in test_cases:
        run_test(test_id, nums, k, expected)

if __name__ == '__main__':
    main()