"""
Given an array of integers citations where citations[i] is the number of citations
 a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that
 the given researcher has published at least h papers that have each been cited at least h times.

Constraints:
    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        """
        Approach - Iterate throught a sorted input, starting with the largest number of citations

        What we know:
         - H Index must be <= len(citations) # Must be less than or equal to the length of thier published works
         - H Index = maximum number of citations from each paper we can fit <= len(citation) to make a maximum h
         - If I’m at index i, there are i + 1 papers seen so far — do they all have at least i + 1 citations?”
        """

        max_bound = len(citations)
        max_h = 0
        citations.sort(reverse=True)  # Sorted in Decending Order

        for i in range(len(citations)):
            if citations[i] >= i + 1:  # If I’m at index i,
                max_h += 1  # there are i + 1 papers seen so far, do they all have at least i + 1 citations?
                # If not, then return
            else:
                return max_h

        return max_h

    """
    Time Complexity  - O(n log n): due to sorted function which uses timesort, n log n operation 
    Space Complexity - O(1): Using constant space and sorting in place 
    """
