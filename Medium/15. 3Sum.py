from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        What we know
            1. Return all Triplets - not just a single set
            2. Solution set cannot contain duplicates indices, i != j != k
            3. Input is not sorted
            4. Output order does not matter
        """

        """
        Approach - need to find x + y + z = 0, if we keep x in place, then iterate over the rest of the list.
        If nothing is found, increment x+1 and repeat until we exhaust all x. If we did find one, then store it in the return list
        Sort the input array first O(n) operation, which allows for two pointer approach L and R for inner loop. 
        """

        result = []
        nums.sort()  # Sort input O(n)

        # Outer loop - for each x
        for i in range(len(nums)):

            # Skip duplicate values of x as we already checked the array for those, also avoids duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            x = nums[i]

            # Inner Loop - L,R pointer approach
            L, R = i + 1, len(nums) - 1

            while L < R:

                curr_sum = nums[L] + nums[R] + x

                if curr_sum == 0:
                    result.append([x, nums[L], nums[R]])
                    # break # No need to break here, as there might be additional combinations with current X

                    # To avoid duplicates, we need to increment L and decrement R while they point to the same values
                    curr_L, curr_R = nums[L], nums[R]
                    L += 1
                    R -= 1

                    # Does not make it triple nested, rather this is an optimization where we are bumping the inner loop variables forward if duplicates found
                    while L < R and nums[L] == curr_L:
                        L += 1
                    while L < R and nums[R] == curr_R:
                        R -= 1

                elif curr_sum > 0:
                    R -= 1
                else:
                    L += 1

        return result

"""
Time Complexity - O(n^2):  Outer loop and inner loop 
Space Complexity - O(k): Where k is the number of unique triplets found and return, theoretically with many combinations possible this can approach O(n^2)  
"""
