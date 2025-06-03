from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # Approach 1 - Utilize 3 pointers, i, j and k, where i = j-1 = k-2.
        # Identify for a given i, there exists a num[j] that is greater than num[i]
        # and do the same for num[j] < num[k]
        # This is brute force, and would yield ~ O(n**3)

        # Approach 2 - Utilize a single loop pass, and keep track of the smallest and
        # second-smallest numbers found, If we found a new smallest or second smallest, then update
        # If we find a third number, then instantly return True
        # If we go through everything, return False.
        # This yields O(n) and O(1) time and space complexities

        if len(nums) < 3:
            return False  # cannot exist as it is less than 3

        smallest, second_smallest = float("inf"), float("inf")
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num < second_smallest:
                second_smallest = num
            elif num > second_smallest:
                return True

        return False