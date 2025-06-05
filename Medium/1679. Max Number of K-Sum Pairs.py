'''
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109
'''

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # Approach - The problem is asking to count the number of pairs which sum to k
        # For each possible value x, it can be paired with k-x, its complement. x + (k-x) = k
        # Total Max Pairs = min(count(x), count(k-x)), which is to say its the minimum of num (x) vs its complement (k-x)
        # Unless that is x = k/2, where the total number of pairs will be floor (count(x)/2)
        # To explain the second part, imagine we had [3, 3, 3] and k=6, then x=k/2 == 3, so total possible pairs will be floor(3/2) = 1
        count = 0
        complements = {nums[0]: 1}  # Initialize with the first complement from num[0]
        for i in range(1, len(nums)):
            complement = k - nums[i]
            curr = nums[i]
            # If we have found a complement, then remove it from the map and count++
            if complement in complements and complements[complement] >= 1:
                complements[complement] -= 1
                count += 1
            else:
                # This is either a new complement, or we've seen it before, so increment value
                complements[curr] = complements.get(curr, 0) + 1

        return count

def main():
    my_solution = Solution()
    answer = my_solution.maxOperations(nums=[1,2,3,4,5], k=5)
    #print(f"answer:{answer}")
    assert(answer == 2)
    answer = my_solution.maxOperations(nums=[3,1,3,4,3], k=6)
    assert(answer == 1)
    print('All tests passed.')


if __name__ == '__main__':
    main()


    """
    Time Complexity - O(n): iterating over the input of length n once
    Space Complexity - O(n): storing a map of roughly ~n size
    """