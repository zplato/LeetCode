# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


def main():
    pass



# This structure ensures the main() function is executed only when the script is run directly, not when imported as a module.
# It's a common practice in Python to organize code and control execution flow
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------#

# Time Complexity: O(n)
# Space Complexity: O(n)