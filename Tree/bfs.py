from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def bfs(root: Optional[TreeNode]):
    if not root:
        return

    queue: list[TreeNode] = [root]

    while len(queue):
        head = queue[0]
        queue = queue[1:]
        print(head.val)
        if head.left is not None:
            queue.append(head.left)

        if head.right is not None:
            queue.append(head.right)


if __name__ == "__main__":
    root = TreeNode(
        val=4,
        left=TreeNode(val=3, left=TreeNode(val=2)),
        right=TreeNode(val=6, left=TreeNode(val=5), right=TreeNode(val=7)),
    )
    bfs(root)