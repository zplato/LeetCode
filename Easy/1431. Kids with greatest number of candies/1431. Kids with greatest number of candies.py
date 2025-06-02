from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Approach 1 - iterate over kids and create an array of max_candies_per_kid Then, and find and store the candy of the kid who has the most originally.
        # Then iterate over the max candy per kid array comparing the max to the original max and create the return boolean array

        # max_orig_candy = 0
        # max_candies = []
        # for candy in candies:
        #     max_orig_candy = max(candy, max_orig_candy)
        #     max_candies.append(candy + extraCandies)
        #
        # return [num_candies >= max_orig_candy for num_candies in max_candies]


        # Approach 2 - Do the same thing, except use max() to find the max in the list a lot easier

        max_orig_candy = max(candies)  # Does the same as above
        return [(candy + extraCandies) >= max_orig_candy for candy in candies]


'''
Both Approaches
Time Complexity - O(n)  - Here we iterate over once to get max_orig and we iterate again to create the return list, so 2*O(n) ~= O(n)
Space Complexity - O(n) - We store and return a list of booleans n length 
'''