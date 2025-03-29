class Solution:
    """
    Problem:
    Given a non-negative integer, you are allowed to swap two digits at most once to get the maximum valued number.
    Return the maximum number you can get.

    Approach:
    - Convert the integer to a list of characters for easier swapping.
    - Use a brute-force approach:
        - Iterate through all pairs of indices (i, j) where i < j.
        - Swap the two digits, convert to int, and check if the number is larger than the current maximum.
        - Swap back to restore the original list and continue.
    - Return the largest number found after checking all possibilities.

    Time Complexity: O(n^2), where n is the number of digits in the number.
                     We check every pair of indices for a possible swap.

    Space Complexity: O(n), for converting the number into a list of characters.
    """

    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        biggest_num = num
        i, j = 0, 1
        while i < len(num_list):
            while j < len(num_list):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                candidate = int("".join(num_list))
                if candidate > biggest_num:
                    biggest_num = candidate
                num_list[i], num_list[j] = num_list[j], num_list[i]  # Swap back
                j += 1

            i += 1
            j = i + 1

        return biggest_num


def main():
    solution = Solution()

    test_cases = [
        (2736, 7236),
        (9973, 9973),
        (98368, 98863),
        (1993, 9913),
        (0, 0),
        (9, 9),
        (91234, 94231),
        (12345, 52341),
    ]

    for i, (num, expected) in enumerate(test_cases, 1):
        result = solution.maximumSwap(num)
        print(f"Test Case {i}: Input = {num}, Output = {result}, Expected = {expected}")
        assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
