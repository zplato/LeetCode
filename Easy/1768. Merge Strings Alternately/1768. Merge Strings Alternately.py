"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Approach 1 - use two pointers for each word and iterate through a loop until both words are finished

        i, j = 0, 0
        result = []  # Using a list here instead of a string
        # Adding to the end of a string rebuilds it each time
        # which causes O(n^2 behavior)

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1

        return ''.join(result)

def main():
    sol = Solution()

    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
        ("hello", "", "hello"),
        ("", "", ""),
        ("a", "b", "ab"),
    ]

    for i, (word1, word2, expected) in enumerate(test_cases, 1):
        result = sol.mergeAlternately(word1, word2)
        print(f"Test Case {i}:")
        print(f"  word1:    \"{word1}\"")
        print(f"  word2:    \"{word2}\"")
        print(f"  Output:   \"{result}\"")
        print(f"  Expected: \"{expected}\"")
        print(f"  Pass:     {result == expected}\n")


if __name__ == "__main__":
    main()



"""
Time Complexity: O(n + m)
    - Where n and m are lengths of word1 and word2
    - One pass through each word

Space Complexity: O(n + m)
    - Building result list of total combined size
"""