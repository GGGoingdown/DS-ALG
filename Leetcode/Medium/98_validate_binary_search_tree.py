# Definition for a binary tree node.
from re import L
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ... 





def main():
    root = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    solution = Solution()
    print(solution.isValidBST(root))


main()