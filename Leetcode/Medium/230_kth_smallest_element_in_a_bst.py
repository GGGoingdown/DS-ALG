# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result: list[int] = []
        self.inorder(root, result)
        return result[k - 1]

    def inorder(self, root: Optional[TreeNode], li: list) -> None:
        if not root:
            return

        self.inorder(root.left, li)
        li.append(root.val)
        self.inorder(root.right, li)


if __name__ == "__main__":
    root = TreeNode(
        val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4)
    )
    solution = Solution()
    k = 1
    print(solution.kthSmallest(root, k))
