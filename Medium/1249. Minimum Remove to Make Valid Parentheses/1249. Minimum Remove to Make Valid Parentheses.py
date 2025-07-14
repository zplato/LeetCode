"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Edge Case 1 - Empty String
        if not s:
            return s

        # An invalid close parenthesis ")" without any prior opening parenthesis
        # An invalid opening parenthesis "(" without any follow on close parenthesis

        # Approach #1 - Iterate through the string and count the number of valid parenthesis

        # counts = {}
        # result = ""
        # i = 0
        # while i < len(s):
        #     char = s[i]
        #     if char == ')' and counts.get('(', 0):
        #         counts['('] -= 1
        #         result += char

        #     elif char == '(':
        #         counts['('] = counts.get('(', 0) + 1
        #         result += char
        #     elif char != "(" and char != ")":
        #         result += char

        #     i += 1

        # # Check if we have any invalid Opening parenthesis left
        # if counts.get('(', 0):
        #     result = result[::-1]
        #     result = result.replace('(', '', counts.get('('))
        #     result = result[::-1]

        # Approach #2 - Utilize a Stack to count unmatched '('
        open_stack = []
        invalid_indices = set()
        i = 0
        while i < len(s):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == ')':
                if len(open_stack) > 0:
                    open_stack.pop()  # Found a match, remove the opening parentheses
                else:
                    invalid_indices.add(i)
            i += 1

        # At this point, the result may still contain invalid open parenthesis
        # These would be the last parenthesis unmatched at the end of the string
        # The delta between length of open_stack
        # print(open_stack)
        # print(invalid_indices)
        invalid_indices.update(open_stack)

        result = []
        for j in range(len(s)):
            if j in invalid_indices:
                continue
            result.append(s[j])

        return ''.join(result)

def main():
    sol = Solution()

    test_cases = [
        ("a)b(c)d", "ab(c)d"),           # One unmatched ')'
        ("(a(b(c)d)", "a(b(c)d)"),       # One unmatched '('
        ("))((", ""),                    # All parentheses are unmatched
        ("lee(t(c)o)de)", "lee(t(c)o)de"),  # One unmatched ')'
        ("a(b(c)d)", "a(b(c)d)"),        # Already valid
        ("", ""),                        # Empty string
        ("abc", "abc"),                  # No parentheses
        ("(a(b))(c)d)", "(a(b))(c)d"),   # One extra ')'
        ("(()", "()"),                   # One unmatched '(' at the end
        ("())()", "()()"),               # One unmatched ')' in the beginning
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = sol.minRemoveToMakeValid(inp)
        print(f"Test Case {i}:")
        print(f"  Input:    \"{inp}\"")
        print(f"  Output:   \"{result}\"")
        print(f"  Expected: \"{expected}\"")
        print(f"  Pass:     {result == expected}\n")


if __name__ == "__main__":
    main()

"""
Time Complexity: O(n) - As we loop over the input twice which is O(2*n) which simplifies to O(n) 
                        NOTE: Constants are dropped in big O notation
Space Complexity: O(n) - we take up the most space when we return the whole string 
"""