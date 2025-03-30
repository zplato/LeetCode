'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

        Approach:
        Use a min heap to maintain the k largest elements seen so far.
        - Push elements into the heap.
        - If heap size exceeds k, pop the smallest.
        - The root of the heap will be the kth largest element.

        Time Complexity: O(n log k)
            - n iterations, each heappush/pop takes O(log k)

        Space Complexity: O(k)
            - Storing at most k elements in the heap
'''

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for num in nums: # O(n) here
            heapq.heappush(min_heap, num) # O(log k) here
            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(log k) here
        return min_heap[0]

def main():
    sol = Solution()

    # Test Case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Test 1 - Expected: 5, Got: {sol.findKthLargest(nums1, k1)}")

    # Test Case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Test 2 - Expected: 4, Got: {sol.findKthLargest(nums2, k2)}")

    # Test Case 3
    nums3 = [1]
    k3 = 1
    print(f"Test 3 - Expected: 1, Got: {sol.findKthLargest(nums3, k3)}")

    # Test Case 4
    nums4 = [7, 10, 4, 3, 20, 15]
    k4 = 3
    print(f"Test 4 - Expected: 10, Got: {sol.findKthLargest(nums4, k4)}")

    # Test Case 5
    nums5 = [99, 99, 99]
    k5 = 2
    print(f"Test 5 - Expected: 99, Got: {sol.findKthLargest(nums5, k5)}")

if __name__ == "__main__":
    main()