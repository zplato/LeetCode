'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Approach 1 - Utilize same approach, two pointers, write and read

        if len(nums) <= 2:
            return len(nums)

        write = 2

        for read in range(2, len(nums)):
            # Check if the current read value is equal to a number we've already written twice, if so then skip it
            if nums[read] == nums[write - 2]:
                continue
            else:
                nums[write] = nums[read]
                write += 1

        return write


def main():
    sol = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]),
        ([1, 1], [1, 1]),
        ([1, 1, 1, 1], [1, 1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([], []),
        ([1], [1]),
        ([1, 1, 2, 2, 2, 3], [1, 1, 2, 2, 3]),
    ]

    print("Testing removeDuplicates (keep at most 2 of each element):\n")
    for i, (input_arr, expected) in enumerate(test_cases):
        arr = input_arr.copy()
        k = sol.removeDuplicates(arr)
        result = arr[:k]
        passed = result == expected
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Test {i+1}: {status}")
        print(f"  Input:    {input_arr}")
        print(f"  Expected: {expected}")
        print(f"  Output:   {result}\n")

if __name__ == "__main__":
    main()


'''
Time Complexity - O(n) - Iterate over the array in a single pass 
Space Complexity - O(1) - Modified in place, no new space utilized 
'''