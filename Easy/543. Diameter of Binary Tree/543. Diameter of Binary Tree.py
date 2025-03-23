from typing import Optional

# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.


def build_tree():
    # Creating tree structure:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # non local variable above the dfs scope
        res = 0

        def dfs(root):
            # We hit this when we are at a non-existant leaf node
            if not root:
                return 0

                # Recursive Calls for L-R DFS
            l = dfs(root.left)  # DFS on left first
            r = dfs(root.right)  # Then Go right

            nonlocal res  # Get the global value
            res = max(res, l + r)  # If we found a greater number (l + r), then lets use it instead

            return 1 + max(l, r) # Add 1 here since we are returning

        dfs(root)
        return res


def main():
    soln = Solution()
    root = build_tree()
    result = soln.diameterOfBinaryTree(root)
    print("Test Case 1 | input: [1,2,3,4,5] | expected: 3 | result: {}".format(result))


# This structure ensures the main() function is executed only when the script is run directly, not when imported as a module.
# It's a common practice in Python to organize code and control execution flow
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------#

# Time Complexity: O(n)     - Visit every node exactly once
# Space Complexity: O(h)    - Comes from the recursion calls stack, where the max height of the call stack is the
#                             height of the tree
