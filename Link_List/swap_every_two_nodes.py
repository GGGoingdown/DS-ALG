class Node:
    def __init__(self, val: int, next = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}, {self.next.__repr__()}"

def swap(list_node: Node):
    head = list_node
    current = head

    while current is not None and current.next is not None:
        current.val, current.next.val = current.next.val, current.val
        current = current.next.next



def main():
    llist = Node(10, Node(10, Node(40, Node(40))))
    print(llist)
    swap(llist)
    print(llist)




main()