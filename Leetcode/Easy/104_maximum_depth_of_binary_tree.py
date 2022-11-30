# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.helper(root, current_count=1)

    def helper(self, root: Optional[TreeNode], current_count: int) -> int:
        if not root:
            return current_count - 1

        left_depth = self.helper(root.left, current_count=current_count + 1)
        right_depth = self.helper(root.right, current_count=current_count + 1)

        return max(left_depth, right_depth)


if __name__ == "__main__":
    tree1 = TreeNode(
        val=1,
        left=TreeNode(val=9),
    )

    solution = Solution()
    result = solution.maxDepth(tree1)
    print(result)
