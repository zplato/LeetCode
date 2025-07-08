from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        Approach 1 - with the input array sorted, we can quickly look for the complement.
        This is O(n^2), given that we iterating over the list, and doing a linear scan each time with complements.values()
        It does work, but is not optimal and doesn't take advantage of the 'sorted' input.
        """

        # # Utilize a Hashmap to store indices, and the complement
        # complements = {}

        # for i in range(len(numbers)):

        #     if target-numbers[i] in complements.values():
        #         keys = [key for key, value in complements.items() if value == target-numbers[i]]
        #         return [keys[0]+1, i+1]

        #     # else its not in complements, so put it there
        #     complements[i] = numbers[i]

        """
        Approach 2 - use two pointers, a L and R pointer which walk the array on the left and right side respectively 
        Once they cross, L >= R, then exit the loop, however this shouldn't happen as we are garunteed exactly one solution
        """

        L, R = 0, len(numbers)-1 # two pointers

        while L < R:
            curr_sum = numbers[L] + numbers[R]

            if curr_sum == target:
                return [L+1, R+1]
            elif curr_sum > target:
                R -= 1
            elif curr_sum <= target:
                L += 1

        return []

    """
    Time Complexity O(n) - iterate through the list once using two pointers
    Space Complexity O(1) - constant space
    """