from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # Lexographically means that the words are sorted in alphabetical order
        # we have to map the characters of the words to order given, for example, order=hlab, where position 0 = h, and 1 = l...

        order_dict = {char: i for i, char in enumerate(order)}  # O(n) operation

        i, j = 0, 1
        while j < len(words):

            word_one, word_two = words[i], words[j]
            correct_order = False
            # Check if the first word index in order_dict is >= second word index in order_dict
            for c1, c2 in zip(word_one, word_two):
                if order_dict[c1] > order_dict[c2]:
                    return False  # Found out of order
                elif order_dict[c1] < order_dict[c2]:
                    correct_order = True
                    break  # found the correct order, so no reason to keep checking (think dictionary order)

            if not correct_order and len(word_one) > len(word_two):
                return False  # Given that word 1 is longer

            # Increment to new words
            i += 1
            j += 1

        return True


"""
Time Complexity: O(M) - where M is equal to the total number of characters, worst case ~O(n^2) 
Space Complexity: O(1) - utilizng constant space 
"""