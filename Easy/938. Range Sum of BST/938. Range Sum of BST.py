from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # Given the root node of a binary search tree and two integers low and high,
        #   return the sum of values of all nodes with a value in the inclusive range [low, high].

        # Do a DFS, and if the value of the node is within the range (inclusive), then add it to the sum
        sum = 0

        def depth_first_search(root):
            nonlocal sum
            if root.val <= high and root.val >= low:
                sum += root.val
            if root.left:
                depth_first_search(root.left)
            if root.right:
                depth_first_search(root.right)

        depth_first_search(root)

        return sum

    """
    Approach:
    ---------
    - Use a recursive Depth-First Search (DFS) traversal starting from the root.
    - For each node:
        - If the node's value is within the given [low, high] range, add it to a running sum.
        - Recursively visit both the left and right children to ensure all nodes are checked.
    - This solution does not leverage pruning and will visit every node in the tree.

    Time Complexity:
    ----------------
    - O(n), where n is the total number of nodes in the tree (each node may be visited once).

    Space Complexity:
    -----------------
    - O(h), where h is the height of the tree (recursion stack).
        - Worst case: O(n) for a skewed tree.
        - Best case: O(log n) for a balanced tree.
    """
