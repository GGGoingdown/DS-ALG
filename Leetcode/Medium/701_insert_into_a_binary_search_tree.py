# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

""" 
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""
import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val=val)
        else:
            root.right = self.insertIntoBST(root.right, val=val)

        return root


def showTree(root: Optional[TreeNode]) -> None:
    if not root:
        return None
    print(root.val)
    if root.left is not None:
        showTree(root.left)
    if root.right is not None:
        showTree(root.right)


def checkBST(root: Optional[TreeNode]) -> None:
    isValidBST(root, min=-math.inf, max=math.inf)


def isValidBST(root: Optional[TreeNode], min: float, max: float) -> None:
    if not root:
        return

    if root.val < min or root.val > max:
        raise ValueError(f"Invalid value {root.val}. ({min}, {max})")

    isValidBST(root.left, min, root.val - 1)
    isValidBST(root.right, root.val + 1, max)


if __name__ == "__main__":
    tree1 = TreeNode(
        val=40,
        left=TreeNode(
            val=20, left=TreeNode(val=10), right=TreeNode(val=30, left=TreeNode(val=19))
        ),
        right=TreeNode(val=60, left=TreeNode(val=50), right=TreeNode(val=70)),
    )

    solution = Solution()
    result = solution.insertIntoBST(tree1, val=25)
    showTree(result)
    checkBST(tree1)
