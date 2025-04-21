

import re

class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach, lets split words into a list, reverse each word in the list and then join the string again.

        s = s.strip()  # Remove leading and trailing whitespace

        s = re.sub(r"\s+", " ", s)  # Replace multiple spaces with single space

        s_list = s.split(" ")  # Split words into a list based on space

        reversed_list = s_list[::-1]  # Reverse the list

        return " ".join(reversed_list)  # Join the list together and add a space in between each item

def run_test(test_id: int, input_str: str, expected: str):
    sol = Solution()
    result = sol.reverseWords(input_str)
    if result == expected:
        print(f"Test {test_id}: PASS")
    else:
        print(f"Test {test_id}: FAIL")
        print(f"  Input:    '{input_str}'")
        print(f"  Expected: '{expected}'")
        print(f"  Got:      '{result}'")

def main():
    test_cases = [
        (1, "the sky is blue", "blue is sky the"),
        (2, "  hello world  ", "world hello"),
        (3, "a good   example", "example good a"),
        (4, "  Bob    Loves  Alice   ", "Alice Loves Bob"),
        (5, "Alice does not even like bob", "bob like even not does Alice"),
        (6, "   ", ""),  # Edge case: all spaces
        (7, "word", "word"),  # Single word
    ]

    for test_id, input_str, expected in test_cases:
        run_test(test_id, input_str, expected)


if __name__ == "__main__":
    main()


"""
Time Complexity: O(n) - n is the length of the input string.
- strip(): O(n)
- re.sub(): O(n)
- split(): O(n)
- reversing list: O(n)
- join(): O(n)

Space Complexity: O(n) - 
- Due to the list of words and the final joined string.
"""