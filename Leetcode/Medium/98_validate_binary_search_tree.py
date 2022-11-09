# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_bst(root, min=-math.inf, max=math.inf)

    def check_bst(self, root: Optional[TreeNode], min: float, max: float) -> bool:
        if not root:
            return True

        if root.val < min or root.val > max:
            return False

        left_result = self.check_bst(root.left, min=min, max=root.val - 1)
        if left_result is False:
            return False
        right_result = self.check_bst(root.right, min=root.val + 1, max=max)
        if right_result is False:
            return False

        return True


def main():
    root = TreeNode(
        5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6))
    )
    solution = Solution()
    print(solution.isValidBST(root))


main()
