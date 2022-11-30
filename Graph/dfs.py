from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root: Optional[TreeNode]):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root: Optional[TreeNode]):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)


if __name__ == "__main__":
    root = TreeNode(
        val=5,
        left=TreeNode(
            val=3, left=TreeNode(val=2, left=TreeNode(val=1)), right=TreeNode(val=4)
        ),
        right=TreeNode(
            val=9,
            left=TreeNode(val=7),
            right=TreeNode(val=13, left=TreeNode(val=12), right=TreeNode(val=16)),
        ),
    )

    # inorder(root)
    # preorder(root)
    postorder(root)