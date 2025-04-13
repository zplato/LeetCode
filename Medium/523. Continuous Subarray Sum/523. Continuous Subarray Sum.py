'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # Approach 1 - iterate through all subarrays using two pointers
        # To check if its a multiple, we can utilize the modulo operator
        # Where %= 0, means that there is no remainder, e.g., a multiple
        # This is not optimal - to slow!!!

        # i, j = 0, len(nums) # initialize pointer values
        # while i < len(nums):
        #     while j > i:
        #         if len(nums[i:j]) <= 1:
        #             break
        #         sub_array_sum = sum(nums[i:j]) # This is x
        #         print(sub_array_sum)
        #         if sub_array_sum % k == 0 and sub_array_sum/k >= 1:
        #             return True # Found a contigous multiple
        #         elif len(nums[i:j]) > 1 and sub_array_sum == 0:
        #             return True

        #         j -= 1

        #     # Reset loop variables
        #     i += 1
        #     j = len(nums)

        # return False # Default Return

        # Approach 2 - Utilize Prefix Sums
        # This returns a sub-array, with all the sums from the first element to the last element

        # Edge Case 1 - Cannot be a subarray with less than 2 elems
        if len(nums) < 2:
            return False

        mod_map = {0: -1}  # hashmap of {mod: index}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num  # Add up the number for each loop
            mod = prefix_sum % k  # Given k will never equal 0

            # Check if we've seen this number before
            if mod in mod_map:
                if i - mod_map[mod] >= 2:
                    return True
            else:
                mod_map[mod] = i

        return False  # Default


# TODO - Revisit this one, its difficult
