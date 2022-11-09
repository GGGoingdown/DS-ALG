# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root


def showTree(root: Optional[TreeNode]) -> None:
    if not root:
        return None
    print(root.val)
    if root.left is not None:
        showTree(root.left)
    if root.right is not None:
        showTree(root.right)


if __name__ == "__main__":
    root = TreeNode(
        val=4,
        left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
        right=TreeNode(val=7),
    )
    solution = Solution()
    result = solution.searchBST(root, 2)
    showTree(result)
