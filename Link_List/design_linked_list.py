from typing import Optional


class LinkedList:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[LinkedList] = None
        self.tail: Optional[LinkedList] = None

    def get(self, index: int) -> int:
        cur_idx = 0
        cur_nod = self.head
        while cur_nod:
            if cur_idx == index:
                return cur_nod.val

            cur_nod = cur_nod.next
            cur_idx += 1

        raise IndexError(f"Out of index: {index}")

    def addAtHead(self, val: int) -> None:
        if self.head:
            tmp = self.head
            self.head = LinkedList(val=val, next=tmp)
            return
        node = LinkedList(val=val)
        self.head = node
        self.tail = node

    def addAtTail(self, val: int) -> None:
        if self.tail:
            node = LinkedList(val=val)
            self.tail.next = node
            self.tail = self.tail.next
            return
        node = LinkedList(val=val)
        self.head = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if (cur_index + 1) == index:
                cur_next_node = cur_node.next
                append_node = LinkedList(val=val, next=cur_next_node)
                cur_node.next = append_node
                return

            cur_node = cur_node.next
            cur_index += 1

        raise IndexError(f"Out of index: {index}")

    def deleteAtIndex(self, index: int) -> None:
        cur_index = 0
        cur_node = self.head
        pre_node: Optional[LinkedList] = None
        while cur_node:
            if cur_index == index:
                next_node = cur_node.next
                if pre_node:
                    pre_node.next = next_node
                else:
                    self.head = next_node
                return

            pre_node = cur_node
            cur_node = cur_node.next
            cur_index += 1

        raise IndexError(f"Out of index: {index}")


def showLinkList(head: Optional[LinkedList]) -> None:
    cur = head
    while cur:
        print(f"Val: {cur.val}")
        cur = cur.next


if __name__ == "__main__":
    my_linked = MyLinkedList()
    my_linked.addAtHead(10)
    my_linked.addAtTail(9)
    my_linked.addAtHead(1)
    my_linked.addAtTail(11)
    my_linked.addAtIndex(1, val=20)
    my_linked.deleteAtIndex(0)
    showLinkList(my_linked.head)
    print(my_linked.get(1))
    my_linked.deleteAtIndex(0)
    print(my_linked.get(1))
