"""
Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        "Approach - Utilize a dictionary of predefined mappings to convert from roman to decimal"

        roman_to_num_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100,
                             "CD": 400, "D": 500, "CM": 900, "M": 1000}


        i = 0
        result = 0

        while i < len(s):
            print(i)
            if i < len(s) - 1:
                # Check if the first two digits are in the dict, if not check the single digit
                if (s[i] + s[i + 1]) in roman_to_num_dict:
                    result += roman_to_num_dict[s[i] + s[i + 1]]
                    print(s[i] + s[i + 1])
                    i += 2
                else:
                    result += roman_to_num_dict[s[i]]
                    i += 1
            else:
                result += roman_to_num_dict[s[i]]
                i += 1

        return result

def main():
    sol = Solution()

    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XLII", 42),
        ("CDXLIV", 444),
        ("MMXXIV", 2024),
        ("DCCCXC", 890),
    ]

    print("Testing romanToInt():\n")
    for i, (roman_str, expected) in enumerate(test_cases, 1):
        result = sol.romanToInt(roman_str)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input:    {roman_str}")
        print(f"  Expected: {expected}")
        print(f"  Output:   {result}\n")


if __name__ == "__main__":
    main()


"""
Time Complexity: O(n) - Iterate through the input string once 
Space Complexity: O(1) - Utilizing Constant space (fixed size map, no dynamic allocations) 
"""