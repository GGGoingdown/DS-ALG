class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.value}, Left -> {self.left.__repr__()}, Right -> {self.right.__repr__()}"


def insert_bstnode(value: int, node: Node):
    if node is None:
        new_node = Node(value)
        return new_node
    elif value < node.value:
        node.left = insert_bstnode(value, node.left)
    elif value > node.value:
        node.right = insert_bstnode(value, node.right)

    return node


def traverse_inorder(node: Node):
    if node.left:
        traverse_inorder(node.left)
    
    print(node.value)
    
    if node.right:
        traverse_inorder(node.right)

def traverse_preorder(node: Node):
    print(node.value)
    if node.left:
        traverse_preorder(node.left)
    
    if node.right:
        traverse_preorder(node.right)

def traverse_postorder(node: Node):
    if node.left:
        traverse_postorder(node.left)

    if node.right:
        traverse_postorder(node.right)

    print(node.value)



def main():
    root = Node(9)
    insert_bstnode(4, root)
    insert_bstnode(20, root)
    insert_bstnode(1, root)
    insert_bstnode(6, root)
    insert_bstnode(15, root)
    insert_bstnode(170, root)

    traverse_inorder(root)

main()