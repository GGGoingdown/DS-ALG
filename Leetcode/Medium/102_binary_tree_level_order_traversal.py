# Definition for a binary tree node.
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        remaining_tree, level_result = self.helper([root])
        result.append(level_result)
        while len(remaining_tree) > 0:
            remaining_tree, level_result = self.helper(remaining_tree)
            result.append(level_result)

        return result

    def helper(self, list_nodes: List[TreeNode]) -> Tuple[List[TreeNode], List[int]]:
        level_value = []
        level_node = []

        for node in list_nodes:
            if node.left:
                level_node.append(node.left)

            if node.right:
                level_node.append(node.right)

            level_value.append(node.val)

        return level_node, level_value


if __name__ == "__main__":
    node = TreeNode(
        val=3,
    )
    solution = Solution()
    print(solution.levelOrder(node))
