'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
'''


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Recursive variables to track max depth seen and current depth
        max_depth, curr = 0, 0

        def DFS(root):
            nonlocal max_depth
            nonlocal curr
            if not root:
                if curr > max_depth:
                    max_depth = curr
                return
            curr += 1
            # Recurse again
            DFS(root.left)
            DFS(root.right)
            curr -= 1

        # Kickoff initial recrusion
        DFS(root)

        return max_depth


# Main function to run tests
def main():
    solution = Solution()

    # Test 1: Depth 3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    # Test 2: Depth 1 (single node)
    tree2 = TreeNode(1)

    # Test 3: Empty tree
    tree3 = None

    # Test 4: Skewed left
    tree4 = TreeNode(1)
    tree4.left = TreeNode(2)
    tree4.left.left = TreeNode(3)
    tree4.left.left.left = TreeNode(4)

    # Expected outputs
    test_cases = [
        (tree1, 3),
        (tree2, 1),
        (tree3, 0),
        (tree4, 4),
    ]

    for i, (tree, expected) in enumerate(test_cases, 1):
        result = solution.maxDepth(tree)
        if result == expected:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL — Expected {expected}, Got {result}")

if __name__ == "__main__":
    main()


'''
Time Complexity: O(n)   - Where we iterate over all nodes in the tree once 
Space Complexity: O(h)  - Where the maximum space of the recursive call stack is defined by the height of the tree
                          Worst case is where h = n, in a skewed tree 
'''