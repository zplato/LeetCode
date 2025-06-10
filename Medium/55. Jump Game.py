"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:\
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Approach 1 - Utilize Greedy Approach, where we iterate through the list starting at position 0,
        # Keeping track of which positions are reachable in another list. If the position is reachable, then:
        # check if the positon it can reach from that position is good, if so, add it to the list, if not don't add it
        # continue iterating until a solution is found.

        # Special cases - 1. if we've hit a 0, then we cannot continue and need to try increment base index += 1
        #               - 2. if our (jump_val + start_idx) or (curr_idx + jump_val) > last_index, then continue ^^
        #               - 3. if len(nums) == 1, then return True - we are already at last index


        # Initialize Variables
        last_idx = len(nums) - 1 # This is our target position
        max_jump = nums[0] # First index is always valid

        # Handle single array index
        if len(nums) == 1: return True

        # loop over base index, i
        for i in range(0, last_idx+1):

            # Check if this is a valid jump location
            if i <= max_jump:

                # Then, since we can jump from here, check if the jump we make is to the last index
                if i + nums[i] >= last_idx:
                    return True

                # This implicitly includes all jump paths from i to nums[i]
                max_jump = max(max_jump, i + nums[i])

        return False


def main():

    assert Solution().canJump([2,3,1,1,4]) == True
    assert Solution().canJump([3,2,1,0,4]) == False

    print('All tests passed.')

if __name__ == '__main__':
    main()


"""
Time Complexity  - O(n): Iterate through the input list of length n
Space Complexity - O(1): Using constant space  
"""