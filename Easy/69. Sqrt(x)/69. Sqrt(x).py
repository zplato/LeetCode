'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

Constraints:
    0 <= x <= 2^31 - 1
'''


class Solution:
    def mySqrt(self, x: int) -> int:

        # edge cases
        if x < 2:
            return x

            # Approach 1  - Given an integer x, we need to find y such that y^2 (or y*y) = x.
        #             Loop over numbers until we find that the square of num is greater
        #             than x. and then return num-1.

        # for num in range(0, 2147483648):
        #     if num*num > x:
        #         return num-1

        # Approach 2 - Utilize Binary Search
        # We can recognize that we're iterating over a sorted input of numbers so binary search makes sense here

        # Need left and right bounds to implement binary search
        low, high = 0, x

        # Loop and adjust the low and high bounds until we zero in on the target
        while low <= high:
            mid = (low + high) // 2  # Cut the search in half, rounding down (floor)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1  # set the new low bound
            elif mid * mid > x:
                high = mid - 1  # set the new high bound

        # At this point we've exited the loop where low > high, and we've search all nums
        # high will be at the largest numerical value, where high * high ~= x^2

        return high

def main():
    solution = Solution()
    test_cases = [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (15, 3),
        (16, 4),
        (2147395599, 46339),  # Near max 32-bit int value
    ]

    for i, (x, expected) in enumerate(test_cases, 1):
        result = solution.mySqrt(x)
        if result == expected:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL — Input: {x}, Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()

'''
Time Complexity:  O(log x)  - Utilizing peform binary search over the range [0, x], where we cut the search space in half on each interation 
Space Complexity: O(1):     - Utilizing fixed number of variables (low, mid and high), so constant space is used  
'''