'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

'''

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Approach - Create sets (O(1) lookups w/sets) out of distinct nums1 and nums2 lists,
        # then create return lists by using list comprehension and return those lists.
        set1, set2 = set(nums1), set(nums2)
        list1 = [x for x in set1 if x not in set2]
        list2 = [y for y in set2 if y not in set1]

        return [list1, list2]

    '''
    Time Complexity - O(n): we iterate over the input lists multiple times, which leads to C*O(n) which reduces to O(n) 
    Space Complexity - O(m + n): where m and n are the number of unique elements in nums1 and nums2 respectively, due to the space 
    used by set1, set2, and the resulting lists.
    '''