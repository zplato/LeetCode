class Solution:
    def isValid(self, s: str) -> bool:

        # prechecks
        if len(s) <= 1:
            return False

        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) == 0 and (char == ')' or char == '}' or char == ']'):
                return False
            else:
                if (stack[-1] == '(' and char != ')') or (stack[-1] == '{' and char != '}') or (
                        stack[-1] == '[' and char != ']'):
                    return False
                else:
                    stack.pop()  # remove the last element as we closed it successfully

        if len(stack) > 0:
            return False  # We have unclosed parenthesis

        return True

def main():
    soln = Solution()
    test_case_1 = "()"
    test_case_2 = "()[]{}"
    test_case_3 = "(]"

    print("Test Case 1 | input: {0} | solution: {1}".format(test_case_1,soln.isValid(test_case_1)))
    print("Test Case 2 | input: {0} | solution: {1}".format(test_case_2, soln.isValid(test_case_2)))
    print("Test Case 3 | input: {0} | solution: {1}".format(test_case_3, soln.isValid(test_case_3)))


# This structure ensures the main() function is executed only when the script is run directly, not when imported as a module.
# It's a common practice in Python to organize code and control execution flow
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------#

# Time Complexity: O(n)
# Space Complexity: O(n)