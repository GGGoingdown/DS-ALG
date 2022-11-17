# Definition for a binary tree node.
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: list[int] = []
        nodes: list[TreeNode] = [root]

        while True:
            nodes, level_val = self.helper(nodes)
            if len(level_val):
                result.append(level_val.pop())

            if not nodes:
                break

        return result

    def helper(self, nodes: list[TreeNode]) -> Tuple[list[TreeNode], list[int]]:
        level_val: list[int] = []
        level_nodes: list[TreeNode] = []
        for node in nodes:

            if node.left is not None:
                level_nodes.append(node.left)

            if node.right is not None:
                level_nodes.append(node.right)

            level_val.append(node.val)

        return level_nodes, level_val


if __name__ == "__main__":
    root = TreeNode(
        val=1,
        left=TreeNode(val=2, right=TreeNode(val=4)),
        right=TreeNode(val=3, right=TreeNode(val=5)),
    )

    solution = Solution()
    result = solution.rightSideView(root)
    print(result)
