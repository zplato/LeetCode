'''
Given an integer, convert it to a Roman numeral.
Constraints: 1 <= num <= 3999
'''

class Solution:

    def intToRoman(self, num: int) -> str:

        int_to_rom = {
            1: "I", 4: "IV", 5: "V",
            9: "IX", 10: "X", 40: "XL", 50: "L",
            90: "XC", 100: "C", 400: "CD", 500: "D",
            900: "CM", 1000: "M"}

        ret = ""
        str_num = str(num)

        # Loop through sorted keys in descending order
        for value in sorted(int_to_rom.keys(), reverse=True):
            while num >= value:
                ret += int_to_rom[value]
                num -= value

        return ret


def main():
    solution = Solution()

    test_cases = [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
        (44, "XLIV"),
        (621, "DCXXI"),
    ]

    print("Running test cases...\n")
    for i, (num, expected) in enumerate(test_cases, 1):
        result = solution.intToRoman(num)
        if result == expected:
            print(f"Test case {i}: PASS")
        else:
            print(f"Test case {i}: FAIL — Input: {num}, Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()


'''
Time Complexity: O(1) - given input bound at constant 1 to 3999. Even with looping and subtracting the iterations are bounded.
                        If unbounded, then we can consider the time complexity to approach O(log n), given that the input size can determine the number of necessary loops 
Space Complexity: O(1) - given we are using a constant space data struct and result string
'''