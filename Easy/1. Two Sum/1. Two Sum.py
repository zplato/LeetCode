'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Approach, utilize a map here, where key=num, and value=index
        num_map = {}

        for index, num in enumerate(nums):
            if target - num in num_map.keys():
                return [num_map[target - num], index]

            num_map[num] = index

        return []  # Default return if no solution

'''
Time Complexity: O(n) - worst case scenario is to loop over the whole input list
Space Complexity: O(n) - worst case is that we store each num in num_map 
'''