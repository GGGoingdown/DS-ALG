class Node:
    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

from typing import Optional

def find_min_node(node: Node) -> int:
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value


def inorder_success(root: Node, node: Node) -> Optional[int]:
    if node.right is not None:
        return find_min_node(node.right)

    succ = None
    while root is not None:
        if  node.value < root.value:
            succ = root
            root = root.left
        elif node.value > root.value:
            root = root.right

        else:
            break

    return succ.value if succ else None


def main():
    root = Node(20)
    root.left = Node(8, left=Node(4), right=Node(12, left=Node(10), right=Node(14)))
    root.right = Node(22)

    temp = root.left.right.right

    succ = inorder_success(root, temp)
    print(f"Inorder successor of {temp.value} is {succ}")

main()