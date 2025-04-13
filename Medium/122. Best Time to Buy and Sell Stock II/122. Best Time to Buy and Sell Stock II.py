'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Edge case - there is no days
        if len(prices) <= 1:
            return 0

        total_profit = 0

        # Approach - as we iterate over the array prices[], we prioritize microtransactions
        # where we trade at the first sign of profitability
        # Then repeat the process and look for another trade we can profit from
        i = 1
        while i < len(prices):

            # check if we can make a profit
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

            i += 1

        return total_profit

        # Time and Space Complexity -
        # Time - O(n) - iterate over the array once
        # Space - O(1) - storing constant data


def run_test(test_id: int, prices: List[int], expected: int):
    sol = Solution()
    result = sol.maxProfit(prices)
    if result == expected:
        print(f"Test {test_id}: PASS")
    else:
        print(f"Test {test_id}: FAIL")
        print(f"  Input:    {prices}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")


def main():
    test_cases = [
        (1, [7,1,5,3,6,4], 7),
        (2, [1,2,3,4,5], 4),
        (3, [7,6,4,3,1], 0),
        (4, [1], 0),
        (5, [], 0),
        (6, [2,1,2,1,2,1,2], 3),
        (7, [3,3,5,0,0,3,1,4], 8),
    ]

    for test_id, prices, expected in test_cases:
        run_test(test_id, prices, expected)


if __name__ == "__main__":
    main()