# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        return self.helper(p, q)

    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is not None and q is not None:
            if p.val == q.val:
                left_result = self.helper(p.left, q.left)
                if not left_result:
                    return False

                right_result = self.helper(p.right, q.right)
                if not right_result:
                    return False

                return True

        return False


if __name__ == "__main__":
    tree1 = TreeNode(val=1, left=TreeNode(val=3))
    tree2 = TreeNode(val=1, right=TreeNode(val=3))

    solution = Solution()
    result = solution.isSameTree(tree1, tree2)
    print(result)
