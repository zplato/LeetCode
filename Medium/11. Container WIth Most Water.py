'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        '''
        Approach 1 - iterate through the array, keeping track of a left candidate and a right candidate (two pointers),
        and the width between the two (r-l). Then, for each candidate, check the area of container using
        candidate_area = min(left,right) * width and if it is max(largest_area, candidate)
        '''

        # Define indexes for left and right
        # l, r = 0, 1
        # arr_length = len(height)
        # max_area = 0

        # Approach 1 - O(n**2) which is to slow and not optimal
        # # Iterate through every combination, this is O(n**2)
        # # Which is not efficient enough
        # while l < arr_length:
        #     while r < arr_length:
        #         # len x width = area and use min b/c bucket is bounded smallest side
        #         candidate_area = min(height[l], height[r]) * (r-l)
        #         max_area = max(max_area, candidate_area)
        #         r += 1

        #     # reset variables for next l
        #     l += 1
        #     r = l + 1
        # return max_area

        '''
        Approach 2 - Same as 1, except we start the right pointer on the right side and utilize a single loop O(n)
        We always move the pointer that points to the min height. By always moving the pointer pointing to the smaller
        height, we avoid wasting effort on containers we already know are limited by that shorter wall. 
        We're essentially narrowing the search space in a way that always has the potential to increase the area.
        '''

        # Define indexes for left and right
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            candidate_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, candidate_area)
            if (height[l] <= height[r]):
                l += 1
            else:
                r -= 1

        return max_area

        '''
        Time Complexity - O(n) - iterate through the array n times 
        Space Complexity - O(1) - storing constant space 
        '''


