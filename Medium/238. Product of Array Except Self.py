from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Using Division Operator - for intution we can look at this approach, which is to get the total product of the array and then divide by the arr[i] position to get the product for that position. Since we cannot do this, we need another way, what can the prefix and suffix product tell us?

        # Initialize with 1's
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        output = []

        # two pointer solution - i for prefix, and j for suffix
        i, j = 1, len(nums) - 2

        # Utilize Prefix and Suffix product, where prefix product[:i] + suffix product[i+1:] = output_arr[i]
        while i < len(nums):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            i += 1
        while j > -1:
            suffix[j] = suffix[j + 1] * nums[j + 1]
            j -= 1

        return [x * y for x, y in zip(prefix, suffix)]


'''
Time Complexity - O(n): making 3 passes n times, which simplifies to O(n)
Space Complexity - O(n): storing 3 arrays total which simplifies 
'''

