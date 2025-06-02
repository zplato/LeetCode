'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        len_flowerbed = len(flowerbed)
        # Catch all for n == 0 (no flowers to plant
        if n == 0:
            return True

            # Catch all for length of 1
        if len_flowerbed == 1 and not flowerbed[0]:
            return n <= 1

        # Utilize a Greedy Approach, where we should prioritizing to plant the flower at the first sign of being able to
        for i in range(len_flowerbed):

            # If we are at the beginning and we can plant
            if i == 0 and not flowerbed[0] and not flowerbed[1]:
                flowerbed[0] = 1
                n -= 1
                if n == 0:
                    return True
                continue

            # Middle and empty
            elif not flowerbed[i] and i < len_flowerbed - 1 and not flowerbed[i - 1] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                continue
            # End and empty
            elif not flowerbed[i] and i == len_flowerbed - 1 and not flowerbed[i - 1]:
                # flowerbed[i] = 1 # Technically don't need this since its our last check
                n -= 1

        return n <= 0

'''
Time Complexity - O(n): we iterate over the input array once
Space Complexity - O(1): we use constant space and are not storing anything
'''

