from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def postorder(root: TreeNode):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)


if __name__ == "__main__":
    tree_node = TreeNode(
        val=4,
        left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
        right=TreeNode(val=6, left=TreeNode(val=5), right=TreeNode(val=7)),
    )

    postorder(tree_node)