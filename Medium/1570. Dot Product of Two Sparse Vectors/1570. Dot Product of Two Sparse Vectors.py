# 1570. Dot Product of Two Sparse Vectors
# Given two sparse vectors, compute their dot product.
from typing import List


# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class SparseVector:
    def __init__(self, nums: List[int]):
        # if num is not zero, then store the number in a index, num hashmap
        self.vector = {index:num for index, num in enumerate(nums) if num}


    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        # Approach #1 - Brute force, iterate over both vectors and multiply their components together, return the result
        # Return the dotProduct of two sparse vectors
        # for i in range(len(self.vector)):
        #     if self.vector[i] == 0 or vec.vector[i] == 0:
        #         continue
        #     result += self.vector[i]*vec.vector[i]

        # Approach #2 - utilize hashmap with comprehension
        # At this point we have two vectors stored as hashmaps, iterate over the one with smaller size since those are the only real values.

        # Using Ternary Approach
        shorter, longer = (self.vector, vec.vector) if len(self.vector) <= len(vec.vector) else (vec.vector, self.vector)

        for key, shorter_val in shorter.items():
            if longer.get(key, 0):
                result += shorter_val*longer[key]

        return result

def main():
    # Test Case 1: Simple vectors with overlap
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
    result1 = v1.dotProduct(v2)
    print(f"Test Case 1:\n  v1: {v1.vector}\n  v2: {v2.vector}\n  Dot Product: {result1} | Expected: 8")  # 2*4

    # Test Case 2: One vector is all zeros
    v3 = SparseVector([0, 0, 0, 0, 0])
    result2 = v1.dotProduct(v3)
    print(f"\nTest Case 2:\n  v1: {v1.vector}\n  v3: {v3.vector}\n  Dot Product: {result2} | Expected: 0")

    # Test Case 3: Dense vs Sparse
    v4 = SparseVector([1, 2, 3, 4, 5])
    v5 = SparseVector([0, 0, 0, 0, 6])
    result3 = v4.dotProduct(v5)
    print(f"\nTest Case 3:\n  v4: {v4.vector}\n  v5: {v5.vector}\n  Dot Product: {result3} | Expected: 30")  # 5*6

    # Test Case 4: Identical vectors
    v6 = SparseVector([0, 1, 0, 2, 3])
    v7 = SparseVector([0, 1, 0, 2, 3])
    result4 = v6.dotProduct(v7)
    print(f"\nTest Case 4:\n  v6: {v6.vector}\n  v7: {v7.vector}\n  Dot Product: {result4} | Expected: 14")  # 1*1 + 2*2 + 3*3

if __name__ == "__main__":
    main()

'''
    Time Complexity: O(n) — where n is the length of nums
    Space Complexity: O(k) — where k is the number of non-zero elements in nums
'''