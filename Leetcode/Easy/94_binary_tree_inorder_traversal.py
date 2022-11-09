from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []
        if not root:
            return result

        self._helper(root, result)
        return result

    def _helper(self, root: Optional[TreeNode], ary: list[int]) -> None:
        if root is None:
            return None

        self._helper(root.left, ary)
        ary.append(root.val)
        self._helper(root.right, ary)


if __name__ == "__main__":
    tree1 = TreeNode(
        val=40,
        left=TreeNode(
            val=20, left=TreeNode(val=10), right=TreeNode(val=30, left=TreeNode(val=19))
        ),
        right=TreeNode(val=60, left=TreeNode(val=50), right=TreeNode(val=70)),
    )

    tree2 = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))

    solution = Solution()
    result = solution.inorderTraversal(tree2)
    print(result)
