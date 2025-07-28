from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        Approach
        Bit of a tricky problem, we have to use two pointers, think two runners running, where we know its a loop if the faster runner eventually laps the slower runner.
        """

        if not head:
            return False

        slow, fast = head, head  # Set them both at the starting line.
        takeSlowStep = False

        while slow.next != None:

            # Every other loop, we take 1 step on slow
            if takeSlowStep:
                slow = slow.next

            if fast != None:
                fast = fast.next

            if slow == fast:
                return True

            takeSlowStep = not takeSlowStep

        return False  # Default Return


"""
Time Complexity  - O(n): iterate through the list of length n once 
Space Complexity - O(1): constant space  
"""


