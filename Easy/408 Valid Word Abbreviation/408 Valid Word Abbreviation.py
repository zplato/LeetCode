class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
        # The lengths should not have leading zeros.

        # non-adjacent means that they substrings cannot be right next to eachother
        # substrings cannot be empty, e.g, nothing should be '0'

        # two pointers
        # i, m = real word
        # j, n = abbrv word
        i = j = 0
        m, n = len(word), len(abbr)

        # iterate through both the original word and abbreviation, pointing at one character at a time
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue  # Same character - so continue
            elif abbr[j] == '0':
                return False  # has leading zeros so return False in this case
            elif abbr[j].isnumeric():
                k = j  # add a third pointer to get the total substr of the number
                while k < n and abbr[k].isnumeric():
                    k += 1

                # get the number from the abbreviation
                number = int(abbr[j:k])

                # update pointers based on the new number
                i += number
                j = k

                # Else if its not the same character, then we know the abbreviation word doesn't match, so return False
            else:
                return False

                # If we went through the entire substrings, and we ended up on the same character, then return true
        return i == m and j == n



def main():
    sol = Solution()

    test_cases = [
        ("internationalization", "i12iz4n", True),
        ("apple", "a2e", False),
        ("substitution", "s10n", True),
        ("substitution", "s010n", False),
        ("word", "4", True),
        ("word", "3d", True),
        ("word", "w1r1", True),
        ("abbreviation", "a10n", True),
        ("abbreviation", "a10x", False),
        ("hello", "h5", False),
    ]

    for word, abbr, expected in test_cases:
        result = sol.validWordAbbreviation(word, abbr)
        print(f"Testing word='{word}', abbr='{abbr}' => Expected: {expected}, Got: {result}, {'PASS ✅' if result == expected else 'FAIL ❌'}")


if __name__ == "__main__":
    main()

"""
LeetCode Problem: Valid Word Abbreviations (408)
URL: https://leetcode.com/problems/valid-word-abbreviation/

Approach:
- Use a two-pointer technique to iterate through both the original string and the abbreviated string (i and j respectively).
- Check if they are the same character, if so then continue
- elif check if the abbreviation starts leading in a '0', if so then return False as we cannot have leading zeros
- elif check if the abbreviation is numeric, if so then get the numeric value, and jump i ahead by that value and jump j ahead by the length of the value as a string
- else they are not the same character, and not a digit, so return False as it clearly doesn't match 

Time Complexity: O(n)
- Worst case is to iterate through the entire string, plus a little more if there is a number at the very end

Space Complexity: O(1)
- Only using integer indices and local variables with no extra data structures.
"""