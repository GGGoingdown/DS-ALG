from re import L
from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.value}, Left -> {self.left.__repr__()}, Right -> {self.right.__repr__()}"

class BST:
    def __init__(self, node: Node):
        self.root = node

    def insert(self, value: int) -> None:
        new_node = Node(value)
        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return 
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = new_node
                    return 
                current_node = current_node.left

    def lookup(self, value: int) -> bool:
        step = 0
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                print(f"Step: {step} times")
                return True
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left

            step += 1

        return False


def insert_bstnode(value: int, node: Node):
    if node is None:
        new_node = Node(value)
        return new_node
    elif value < node.value:
        node.left = insert_bstnode(value, node.left)
    elif value > node.value:
        node.right = insert_bstnode(value, node.right)

    return node

def search_bstnode(value: int, root: Node) -> bool:
    print("Search ")
    if root is None:
        return False
    elif root.value == value:
        return True
    elif value < root.value:
        return search_bstnode(value, root.left)
    else:
        return search_bstnode(value, root.right)

def find_min_node(node: Node) -> Node:
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left

    return current_node

def delete_bstnode(value: int, root: Node) -> Node:
    if root is None:
        return root

    if value < root.value:
        root.left = delete_bstnode(value, root.left)
    elif value > root.value:
        root.right = delete_bstnode(value, root.right)

    else:   
        # The Node is wanted to delete
        # If Only one child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # With two child
        temp: Node = find_min_node(root.right)
        root.value = temp.value
        root.right = delete_bstnode(temp.value, root.right)
    
    return root





def main():
    root = Node(9)
    insert_bstnode(4, root)
    insert_bstnode(20, root)
    insert_bstnode(1, root)
    insert_bstnode(6, root)
    insert_bstnode(15, root)
    insert_bstnode(170, root)


main()