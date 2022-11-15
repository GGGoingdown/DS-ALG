# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Get p and q 最小值與最大值
        min_value = min(p.val, q.val) 
        max_value = max(p.val, q.val)

        cur_node = root

        while cur_node:
            # 如果比較現node值剛好是一左一右的話(因為是BST) 則返回現在的node
            if min_value < cur_node.val and max_value > cur_node.val:
                return cur_node

            # 如果現在的node值與最小或最大值相同的話 則返回現在的node
            if min_value == cur_node.val or max_value == cur_node.val:
                return cur_node

            # 
            if min_value < cur_node.val and max_value < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return cur_node


if __name__ == "__main__":
    tree1 = TreeNode(
        val=6,
        left=TreeNode(
            val=2,
            left=TreeNode(val=0),
            right=TreeNode(val=4, left=TreeNode(val=3), right=TreeNode(val=5)),
        ),
        right=TreeNode(
            val=8,
            left=TreeNode(val=7),
            right=TreeNode(
                val=9,
            ),
        ),
    )

    solution = Solution()
    result = solution.lowestCommonAncestor(tree1, p=TreeNode(val=8), q=TreeNode(val=2))
    print(result.val)
