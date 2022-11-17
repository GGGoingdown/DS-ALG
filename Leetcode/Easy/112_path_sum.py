# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path: list[int] = []

        return self.backtracking(root, path, targetSum)

    def backtracking(
        self, root: Optional[TreeNode], path: list[int], targetSum: int
    ) -> bool:
        if not root:
            return False

        path.append(root.val)

        if root.left is None and root.right is None and sum(path) == targetSum:
            return True

        if self.backtracking(root.left, path, targetSum):
            return True

        if self.backtracking(root.right, path, targetSum):
            return True

        path.pop()
        return False


if __name__ == "__main__":
    root = TreeNode(
        val=5,
        left=TreeNode(
            val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))
        ),
        right=TreeNode(
            val=8, left=TreeNode(val=13), right=TreeNode(val=4, right=TreeNode(val=1))
        ),
    )

    solution = Solution()
    print(solution.hasPathSum(root, 21))