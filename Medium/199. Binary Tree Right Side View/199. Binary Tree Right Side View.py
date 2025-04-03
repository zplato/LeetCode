# Definition for a binary tree node.
from typing import Optional, List

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        # Approach 1 - Utilize DFS where we go right first
        # If we are at our max depth, then we know this node is visible
        # from the right.

        # The key here is to keep depth relative to the current recursive call
        # another key is to know that max_depth == len(output)

        if root == None:
            return []

        output = [root.val]
        depth = 0

        def DFS(node, depth):
            if not node:
                return


            # If we are officially 1 deeper than our current output
            if depth == len(output):
                output.append(node.val)

            DFS(node.right, depth+1)
            DFS(node.left, depth+1)

        DFS(root, 0)

        return output

def build_tree(nodes):
    """ Helper function to build tree from list (BFS level-order style) """
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)

        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root


def main():
    s = Solution()
    test_cases = [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1, 2, 3, 4], [1, 3, 4]),
        ([1, 2, 3, None, 5, 6], [1, 3, 6]),
    ]

    for i, (tree_list, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        result = s.rightSideView(root)
        print(f"Test Case {i}: {'PASS' if result == expected else 'FAIL'}")
        print(f"  Input: {tree_list}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

if __name__ == "__main__":
    main()

'''
Time Complexity: O(n)
- We visit every node in the binary tree exactly once during DFS traversal.

Space Complexity: O(h)
- `h` is the height of the tree.
- This is the maximum depth of the recursion stack in the worst case (e.g., a skewed tree).
- The `output` list stores at most `h` elements (one per level), but the space complexity is dominated by the call stack.
'''