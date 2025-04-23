'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Constraints:
    1 <= n <= 231 - 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:

        seen_nums = set()

        while n != 1:
            n = sum(int(x) ** 2 for x in str(n))
            if n in seen_nums:
                return False  # looped
            seen_nums.add(n)

        return True

def main():
    solution = Solution()

    test_cases = {
        19: True,
        2: False,
        1: True,
        7: True,
        4: False,
        100: True,
        1111111: True,
        989: True,
        100000: True,
        4444444: False,
        9999999: False,
        1000000000: True
    }

    for n, expected in test_cases.items():
        result = solution.isHappy(n)
        print(f"Test case isHappy({n}): {'PASSED' if result == expected else 'FAILED'} (Expected {expected}, got {result})")

if __name__ == "__main__":
    main()


'''
Time Complexity O(log n)    - per iteration due to digit splitting and squaring, but the total number of unique numbers you might see before a cycle starts or you reach 1 is bounded (typically less than 1000 for all 32-bit integers). 
                                So, it's often said to be O(1) in practice. 
Space Complexity O(log n)   - Also O(1) in practice due to the bounded number of seen values.
'''