class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Example Palindrome - hannah
        # In palindromes, the reverse string must match the current string


        if s == s[::-1]:
            # If its already equal to its reverse
            return True

            # Valid solution but to slow

        # Attempt 1 - Brute force approach using 1 pointer
        # for i in range(len(s)):
        #     temp_s = s[:i] + s[i+1:] # everything up to i and everything after i 

        #     # With a character removed, check to see if the string equals its reverse 
        #     if temp_s == temp_s[::-1]:
        #         return True 

        # Attempt 2 - utilize two pointers 
        # Utilize two pointers, one on each end of the string which allows us the need to only iterate through half of the string 
        # Compare the values of each pointer, if they are equal then continue 
        #   else if they are not equal, then remove one of the values and check if its a palindrome 

        # Create a function to iterate through and check if the strings match 
        # Left is a pointer to the left substring and right is a pointer to the right substring 
        def is_sub_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i = 0
        j = len(s) - 1

        while i < j:

            # Check for a palindrome 

            # Method 1 - This is to slow b/c it reverses the whole string causing O(n^2) behavior 
            # Not the same character! s[i] != s[j]
            # Lets try to remove them one at a time to see if it makes a valid palindrome
            # if s[i] != s[j]:
            # remove_i = s[:i] + s[i+1:]
            # remove_j = s[:j] + s[j+1:]
            # if remove_i == remove_i[::-1] or remove_j == remove_j[::-1]:
            #     return True

            # If we remove the non-matching character (left or right) and then check if the substrings match
            if s[i] != s[j]:
                if is_sub_palindrome(i + 1, j) or is_sub_palindrome(i, j - 1):
                    return True
                else:
                    return False

            i += 1
            j -= 1

        return True # String is already a palindrome without removing a character

def main():
    sol = Solution()

    test_cases = [
        ("abca", True),
        ("racecar", True),
        ("deeee", True),
        ("abcdef", False),
        ("a", True),
        ("", True),
        ("cbbcc", True),  # remove one character 'c' from either end
        ("abcba", True),
        ("ebcbbececabbacecbbcbe", True)  # Long test from LeetCode
    ]

    for idx, (test_input, expected_output) in enumerate(test_cases, 1):
        result = sol.validPalindrome(test_input)
        print(
            f"Test Case {idx} | input: '{test_input}' | expected: {expected_output} | result: {result} | {'✅' if result == expected_output else '❌'}")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------#

"""
LeetCode Problem: Valid Palindrome II (680)
URL: https://leetcode.com/problems/valid-palindrome-ii/

Approach:
- Use a two-pointer technique to compare characters from both ends of the string.
- On mismatch, check if skipping either the left or right character leads to a palindrome.
- Use a helper function to verify palindromes in subranges without additional string slicing.

Time Complexity: O(n)
- The main loop and potential helper palindrome check both run in linear time.

Space Complexity: O(1)
- Only using integer indices and local variables with no extra data structures.
"""