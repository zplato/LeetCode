'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''


class Solution:
    def reverseVowels(self, s: str) -> str:

        # Utilize a set for O(1) lookup and add uppercase to not need an unnecessary call to lower()
        vowels = set('aeiouAEIOU')

        # Approach, check letters and if they in the list of vowels then store them. Then iterate over the original word again, and utilize the reversed list to replace vowels with the reversed vowels.

        my_vowels = [c for c in s if c in vowels]

        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + my_vowels.pop() + s[i + 1:]

        return s

'''
Time Complexity - O(n) - iterate over the string C * O(n) which simplifies to O(n) 
Space Complexity - O(n) - we are storing the input string n length 
'''