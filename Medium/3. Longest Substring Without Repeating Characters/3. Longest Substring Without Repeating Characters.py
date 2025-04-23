'''
Given a string s, find the length of the longest substring without duplicate characters.
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        if len(s) == 1:
            return 1

            # Approach 1 - Brute Force, Check all possible substrings using nested loops
        # n = len(s)
        # max_len = 0
        # for i in range(n): # start index
        #     # Short circuit here as we know that all remaining substr are smaller than what works
        #     if max_len >= n - i:
        #         return max_len
        #     for j in range(i + 1, n + 1): # end index
        #         sub_str = s[i:j]
        #         if len(sub_str) == len(set(sub_str)):
        #             if len(sub_str) > max_len:
        #                 max_len = len(sub_str)

        # return max_len

        # Approach 2 - Utilize Sliding Window, single loop with L and R pointers

        left, right, max_len = 0, 0, 0
        seen_chars = set()

        while right < len(s):
            # As long as we have a duplicate in the list, then
            # remove starting at the left
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            seen_chars.add(s[right])
            max_len = max(max_len, len(s[left:right + 1]))

            right += 1

        return max_len
def main():
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)

    solution = Solution()

    test_cases = [
        ("abcabcbb", 3),     # "abc"
        ("bbbbb", 1),        # "b"
        ("pwwkew", 3),       # "wke"
        ("", 0),             # empty string
        ("abcdef", 6),       # all unique
        ("abba", 2),         # "ab" or "ba"
        ("a", 1),            # single char
        ("dvdf", 3),         # "vdf"
    ]

    print("Running test cases...\n")
    for i, (inp, expected) in enumerate(test_cases, 1):
        result = solution.lengthOfLongestSubstring(inp)
        if result == expected:
            print(f"Test case {i}: PASS")
        else:
            print(f"Test case {i}: FAIL — Input: {inp}, Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
'''
Time Complexity: O(n) - Iterate through the string once, where each character is visited at most twice, by right and left pointers. 
                        Since its worst case O(2n) it simplifies to O(n) 
Space Complexity: O(min(n, m))  - 'seen_chars' stores at most 'm' unique characters, where 'm' is the size of character set
                                  If all the input is unique characters, then this essentially becomes O(n)
                                  If its only ASCII characters, then this effectively becomes O(1) since its bounded  
'''