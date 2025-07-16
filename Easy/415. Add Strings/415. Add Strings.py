class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1)-1, len(num2)-1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

            # Handle index bounds as we iterate over both numbers at the same time
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            # Do the math - even if carry is the only thing left we handle it until carry = 0
            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))


            # Every Loop we decrement
            i -= 1
            j -= 1

        return ''.join(reversed(result))

        """
        Time Complexity - O(n): Where we iterate over the longest string n
        Space Complexity - O(k): where we create a list of num1 (n) and num2 (m) length given the worst case scenario, e.g., 999 + 999 = new list of lenght k
        """