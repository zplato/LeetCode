'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        output = []

        # Edge Case #1 - Single Interval
        if len(intervals) < 2:
            return intervals

            # Approach #1 - Brute Force - Works but slow O(n^2)
        intervals.sort()  # Sort the input by first point
        i, j = 0, 1  # utilize two pointers, two loops
        while j < len(intervals):
            # Think of overlap on a number line - where two lines overlap
            if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                merged_arr = [min(intervals[i][0], intervals[j][0]), max(intervals[i][1], intervals[j][1])]
                # Remove the two intervals and insert the merged array
                del intervals[j]
                del intervals[i]
                intervals.insert(i, merged_arr)
            # else, does not overlap
            else:
                i += 1
                j = i + 1

        return intervals

def main():
    s = Solution()
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 10], [2, 6], [3, 5], [7, 9]], [[1, 10]]),
        ([[1, 4]], [[1, 4]]),
        ([[1, 4], [0, 2], [3, 5], [7, 8]], [[0, 5], [7, 8]]),
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = s.merge(intervals)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        passed = result_sorted == expected_sorted
        print(f"Test Case {i}: {'PASS' if passed else 'FAIL'}")
        print(f"  Input: {intervals}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

if __name__ == "__main__":
    main()

'''
Time Complexity: O(n^2) - due to sorting and del + insertions 
Space Complexity: O(n)
'''