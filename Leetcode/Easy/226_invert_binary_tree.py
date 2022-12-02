# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)

        return root


def inorderTree(root: Optional[TreeNode]) -> None:
    if not root:
        return None

    inorderTree(root.left)
    print(root.val)
    inorderTree(root.right)


if __name__ == "__main__":
    tree1 = TreeNode(
        val=4,
        left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
        right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)),
    )

    solution = Solution()
    result = solution.invertTree(tree1)

    inorderTree(result)
