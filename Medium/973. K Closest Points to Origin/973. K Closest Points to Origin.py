'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Utilize a Max Heap - where the largest number is sorted to the top of the heap
        # To do this, we multiply by the distance by -1, in effect making it the smallest number
        # Which gets sorted to the top via heappush()

        heap = []

        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2) * -1
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the largest element here

        return [tuple[1] for tuple in heap]

def main():
    s = Solution()
    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
        ([[1, 2], [2, 1], [-1, -1], [-2, -2]], 2, [[-1, -1], [-2, -2]]),
        ([[0, 0]], 1, [[0, 0]])
    ]

    for i, (points, k, expected) in enumerate(test_cases, 1):
        result = s.kClosest(points, k)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        print(f"Test Case {i}: {'PASS' if result_sorted == expected_sorted else 'FAIL'}")
        print(f"  Output: {result}\n  Expected: {expected}\n")

if __name__ == "__main__":
    main()


'''
Time Complexity - O(n log k) - where we iterate over all the points once, and then insert and pop off the heap
Space Complexity - O(k) - where the heap is of size k items, which is a subset of n 
'''