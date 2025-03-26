from typing import List

class Solution:
    """
    Problem:
    A peak element is an element that is strictly greater than its neighbors.
    Given an input array `nums`, return the index of any one of its peak elements.
    The array may contain multiple peaks; returning the index of any one of them is valid.
    For elements at the boundaries, only one neighbor needs to be considered.

    Approach:
    - Handle the single-element edge case immediately.
    - Iterate through the list linearly:
        - Check if the current element is a peak by comparing it to neighbors.
        - Pay special attention to the first and last indices.
    - Return the index of the first found peak.

    Time Complexity: O(n), where n is the length of the input list.
    Space Complexity: O(1), as we are using constant extra space.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        # Since we just have to return the index to ANY of the peaks, we can return the index of the first one we find
        i = 0
        while i < len(nums):
            # Handle Edge Cases
            # Edge Case 1 - single number array
            if len(nums) == 1:
                return i # 0 element since
            # Edge case 2 - Index 0 greater than Index 1
            elif i == 0:
                if nums[i] > nums[i+1]:
                    return i
            # Edge case 3 - if we are on the last num, and its greater than the previous num
            elif i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                    return i
            i += 1


def main():
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 1], [2]),  # Peak at index 2
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),  # Peaks at index 1 or 5
        ([1], [0]),  # Single element
        ([2, 1], [0]),  # Peak at index 0
        ([1, 2], [1]),  # Peak at index 1
        ([5, 10, 20, 15], [2]),  # Peak at index 2
        ([10, 20, 15, 2, 23, 90, 67], [1, 5]),  # Peaks at index 1 or 5
    ]

    for i, (nums, expected_possible) in enumerate(test_cases, 1):
        result = solution.findPeakElement(nums)
        print(f"Test Case {i}: Input = {nums}, Output = {result}, Expected = one of {expected_possible}")
        assert result in expected_possible, f"Test case {i} failed: got {result}, expected one of {expected_possible}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
