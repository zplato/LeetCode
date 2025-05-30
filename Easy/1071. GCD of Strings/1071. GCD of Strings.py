import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Approach - Iterate over the shorter string, checking the against the original string + all substrings for division. Return on the first sign of division the substr
        if str1 + str2 != str2 + str1:
            return ""

        len1, len2 = len(str1), len(str2)
        gcd = math.gcd(len1, len2)
        return str1[:gcd]