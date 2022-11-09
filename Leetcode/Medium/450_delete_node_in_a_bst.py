""" 
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

"""

# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key=key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key=key)
        else:
            if root.left is None:  # If left node is None
                return root.right
            elif root.right is None:  # If right node is None
                return root.left
            else:
                # With left and right node, find the minimum number in right side node
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, key=minNode.val)

        return root

    def findMinNode(self, root: TreeNode) -> TreeNode:
        cur = root
        while cur.left is not None:
            cur = cur.left

        return cur


def inOrderTree(root: Optional[TreeNode]) -> None:
    if not root:
        return None

    inOrderTree(root.left)
    print(root.val, end=",")
    inOrderTree(root.right)


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
        val=5,
        left=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=4)),
        right=TreeNode(val=6, right=TreeNode(val=7)),
    )
    print("Before deleting")
    checkBST(tree1)
    inOrderTree(tree1)
    solution = Solution()
    result = solution.deleteNode(tree1, key=1)
    print("")
    print("After deleting")
    checkBST(result)
    inOrderTree(result)
