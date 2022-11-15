# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        return self.dfs(root, subRoot)

    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if self.checkIsSameTree(root, subRoot):
                return True

        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)

    def checkIsSameTree(
        self, root: Optional[TreeNode], subTree: Optional[TreeNode]
    ) -> bool:
        if not root and not subTree:
            return True

        if (root and not subTree) or (not root and subTree):
            return False

        if root.val != subTree.val:
            return False

        return self.checkIsSameTree(root.left, subTree.left) and self.checkIsSameTree(
            root.right, subTree.right
        )


def traversalTree(root: Optional[TreeNode]) -> None:
    if not root:
        return

    traversalTree(root.left)
    print(root.val)
    traversalTree(root.right)


if __name__ == "__main__":
    root = TreeNode(
        val=1,
        left=TreeNode(val=1),
    )

    subRoot = TreeNode(val=1)

    solution = Solution()
    result = solution.isSubtree(root, subRoot)
    print(result)
    # result = solution.isSubtree(root=root, subRoot=subRoot)
    # print(result)
