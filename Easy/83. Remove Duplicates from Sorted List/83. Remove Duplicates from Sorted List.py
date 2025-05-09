

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # List is already sorted - so we need to just remove the nodes whose value equals the head value
        curr = head

        while curr is not None and curr.next is not None:

            if curr.next.val == curr.val:
                curr.next = curr.next.next  # bypass this node in the chain as it has the same value
            else:
                curr = curr.next  # i += 1

        return head


def list_to_linkedlist(elements):
    dummy = ListNode(0)
    curr = dummy
    for el in elements:
        curr.next = ListNode(el)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def main():
    sol = Solution()

    # Example input: [1, 1, 2, 3, 3]
    test_input = list_to_linkedlist([1, 1, 2, 3, 3])
    result = sol.deleteDuplicates(test_input)

    # Expected output: [1, 2, 3]
    print(linkedlist_to_list(result))  # Output should be: [1, 2, 3]

if __name__ == "__main__":
    main()


'''
Time Complexity - O(n): worst case it we iterate through the whole list of length n
Space Complexity - O(1): we utilize constant space as nothing is stored 
'''