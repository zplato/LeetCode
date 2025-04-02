"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Edge case n == 0
        if n == 0:
            return 1

        # Approach 1 - Brute Force
        # O(n) solution here - to slow for leetcode
        # init_x = x
        # for i in range(1, abs(n)):
        #     x = x * init_x

        # if n > 0:
        #     return x
        # else:
        #     return 1/x

        # Approach 2 - Use Exponentiation by Squaring
        # We can actually divide the exponent by two, and for everytime we do that, we actually can double the multiplied value
        # For example, 2^4 = 4^2, where we can divide the 4 by two and multiply the base

        # handle negative exponent
        if n < 0:
            x = 1 / x  # Negative so flip the exponent
            n *= -1  # This is to make it a positive num

        # So we are going to loop decrementing n, using the squaring of an exponent

        result = 1
        base = x  # Initialize to x
        while n:
            # If we hit a point where exponent is odd, then we add in the base
            if n % 2 == 1:
                result *= base

            base *= base  # Actually double the exponent

            # Loop decrementor
            n //= 2  # take the floor - return the integer result
            # print(f"n: {n}, base: {base}, result: {result}")

        return result


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


def main():
    s = Solution()
    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (1.0, 2147483647, 1.0),
        (0.00001, 2147483647, 0.0),  # LeetCode edge case
        (2.0, 0, 1.0),
        (-2.0, 3, -8.0),
        (-2.0, 2, 4.0),
    ]

    for i, (x, n, expected) in enumerate(test_cases, 1):
        result = s.myPow(x, n)
        passed = abs(result - expected) < 1e-4  # Tolerance for float comparison
        print(f"Test Case {i}: {'PASS' if passed else 'FAIL'}")
        print(f"  Input: x={x}, n={n}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")


if __name__ == "__main__":
    main()

'''
Time Complexity: O(log n) - Loops over a subset of n
Space Complexity: O (1) - Constant Space 
'''