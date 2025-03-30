"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(root):

            nonlocal lca
            left, right = False, False

            if root.left:
                left = DFS(root.left)
            if root.right:
                right = DFS(root.right)
            # First condition returns true if in seperate subtrees,
            # OR if they are in the same subtree
            if (left and right) or ((root == p or root == q) and (left or right)):
                lca = root  # The LCA !
                return True

            if root == p or root == q or left or right:
                return True

            return False

        lca = root  # initialize to root
        DFS(root)

        return lca


def main():
    # Helper to build the tree:
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4

    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n1.left = n0
    n1.right = n8
    n2.left = n7
    n2.right = n4

    sol = Solution()

    # Test Case 1: LCA of 5 and 1 is 3
    result = sol.lowestCommonAncestor(n3, n5, n1)
    print(f"LCA of {n5.val} and {n1.val} is {result.val} (Expected: 3)")

    # Test Case 2: LCA of 6 and 4 is 5
    result = sol.lowestCommonAncestor(n3, n6, n4)
    print(f"LCA of {n6.val} and {n4.val} is {result.val} (Expected: 5)")

    # Test Case 3: LCA of 7 and 8 is 3
    result = sol.lowestCommonAncestor(n3, n7, n8)
    print(f"LCA of {n7.val} and {n8.val} is {result.val} (Expected: 3)")

    # Test Case 4: LCA of 2 and 4 is 2
    result = sol.lowestCommonAncestor(n3, n2, n4)
    print(f"LCA of {n2.val} and {n4.val} is {result.val} (Expected: 2)")

    # Test Case 5: LCA of 6 and 6 is 6 (node with itself)
    result = sol.lowestCommonAncestor(n3, n6, n6)
    print(f"LCA of {n6.val} and {n6.val} is {result.val} (Expected: 6)")

if __name__ == "__main__":
    main()

"""
    Time Complexity: O(n)
        - Visits each node once during DFS.
    
    Space Complexity: O(h)
        - h is the height of the tree.
        - Due to the recursion stack, worst case is O(n) for skewed tree,
          best case is O(log n) for balanced tree.
"""