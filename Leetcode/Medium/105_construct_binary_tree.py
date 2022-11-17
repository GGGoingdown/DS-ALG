# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(
            preorder=preorder[1 : mid + 1], inorder=inorder[:mid]
        )
        root.right = self.buildTree(
            preorder=preorder[mid + 1 :], inorder=inorder[mid + 1 :]
        )

        return root


def traversalTree(root: Optional[TreeNode]):
    if not root:
        return

    print(root.val)
    traversalTree(root.left)
    traversalTree(root.right)


if __name__ == "__main__":
    preorder: list[int] = [3, 9, 20, 15, 7]
    inorder: list[int] = [9, 3, 15, 20, 7]

    solution = Solution()
    result = solution.buildTree(preorder, inorder)
    traversalTree(result)
