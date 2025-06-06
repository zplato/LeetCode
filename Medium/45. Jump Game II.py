"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""


from typing import List


def jump(nums: List[int]) -> int:

    """
    Approach 1 - Its guaranteed that we can reach nums[n-1], which is the last index. We can utilize the same exact algorithm
    developed in jump game 1, where we take a greedy approach. We know we can actually get to any number between the current
    num and the jump distance. We store max distance and update it for every position we walk, until we reach or exceed
    the final index. One difference here is that we keeping track of the NUMBER of jumps to reach the end

    IMPORTANT: This solves if we can make it across the finish line, but doesn't solve it with the 'fewest' jump
    """

    # Edge Case, where we have a single index list
    # if len(nums) == 1:
    #     return 0

    # Approach 1
    # max_distance = 0
    # jump_count = 0
    # for i in range(0, len(nums)):

    #     if max_distance < i + nums[i]:
    #         max_distance = max(max_distance, i + nums[i])
    #         jump_count += 1

    #     if max_distance >= len(nums)-1:
    #         return jump_count

    # return jump_count

    """
    Approach 2 - We once again utilize a greedy approach, where we jump to the largest number that we can, 
    and continue jumping to the next largest number. If there are multiple large numbers, we jump to the one with the index 
    furthest away from the start
    """

    # i = 0
    # jump_count = 0
    # while i < len(nums):

    #     # Check if we made it
    #     if i == len(nums)-1:
    #         return jump_count
    #     # or check if we can jump to it directly from here
    #     elif i + nums[i] >= len(nums)-1:
    #         jump_count += 1
    #         return jump_count

    #     # If we haven't made it, and can't jump to it from here, then lets figure out the furthest jump we can make

    #     curr_jump_list = nums[i+1:i+nums[i]+1]      # This gives us the total positions we can jump to
    #                                                 # in between where we are and our furthest jump

    #     max_idx, max_distance = 0, 0

    #     for j in range(0, len(curr_jump_list)):
    #         if curr_jump_list[j] + j > max_distance:
    #             max_distance = curr_jump_list[j] + j
    #             max_idx = j+1

    #     # Make the jump to the furthest place we can
    #     i += max_idx
    #     jump_count += 1

    #     # Debugging Support
    #     # print(i)
    #     # print(f"max_idx: {max_idx}")
    #     # print(curr_jump_list)
    #     # print(jump_count)

    # return -1 # should never get here as the description always promises to have a solution

    """
    Time Complexity - O(n^2): We are iterating over the entire list of length n, and 
    then iterating over sublists - at worst case n*n
    Space Complexity - O(n): We are creating subset lists at worst case length n 
    """

    # Approach 3 - Utilize a Sliding window "max_jump", where we iterate over our current jump and
    # update max_jump to be the max jump possible from our current jump window.

    jump_count = 0
    max_jump = 0  # farthest possible jump
    current_end = 0

    # Its important here that we iterate through every i, to capture the max_jump within the jump window
    for i in range(len(nums) - 1):
        max_jump = max(max_jump, i + nums[i])

        if i == current_end:
            jump_count += 1
            current_end = max_jump

    return jump_count

    """
    Time Complexity - O(n): Iterate over the input once
    Space Complexit - O(1): Storing only a few variables using constant space 
    """
