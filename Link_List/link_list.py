class Node:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"{self.value}, {self.next.__repr__()}"


class LinkedList:
    def __init__(self, value: int) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def traverse_index(self, index: int) -> Node:
        if index >= self.length:
            raise IndexError(f"Out of index")

        count = 0
        current_node = self.head
        while count != index-1:
            current_node = current_node.next
            count += 1
        return current_node

    def insert_front(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_tail(self, value: int) -> None:
        new_node = Node(value)
        self.tail.next = new_node
        self.length += 1

    def insert_index(self, value: int, index: int) -> None:
        if index == 0:
            new_node = Node(value, next=self.head)
            self.head = new_node
        else:
            leader = self.traverse_index(index)
            new_node = Node(value, next=leader.next)
            leader.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            leader = self.traverse_index(index)
            leader.next = leader.next.next
        self.length -= 1

    def reverse(self) -> None:
        if self.length == 1:
           return

        first = self.head
        self.tail = self.head
        second = first.next
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first



def get_items(head: Node, n: int) -> int:
    current = head
    count = 0
    while current != None:
        if count == n:
            return current.value

        current = current.next
        count += 1
    raise Exception("Out of link")


def search(head: Node, value: int) -> bool:
    current = head

    while current != None:
        if current.value == value:
            return True

        current = current.next
    return False
 

def insert_front(head: Node, value: int) -> Node:
    new_head = Node(value, next=head)
    return new_head

def insert_tail(head: Node, value: int) -> Node:
    current = head
    while current is not None:
        next = current.next
        if next is None:
            break
        current = next
    
    if current is not None:
        current.next = Node(value)
        return head
    else:
        head = Node(value)
        return head


def insert(head: Node, idx: int, value: int) -> None:
    pre = head
    for _ in range(0, idx - 1):
        pre = pre.next
        if pre == None:
            break

    new_node = Node(value)
    new_node.next = pre.next
    pre.next = new_node
    return None


def remove(head: Node, value: int) -> None:
    current = head
    if current.value == value:
        head = current.next
        current.next = None
        return 

    while current != None:
        if current.value == value:
            break
        previous = current
        current = current.next
    if current is not None:
        previous.next = current.next


def main():
    link_list = LinkedList(5)
    link_list.insert_front(10)
    link_list.insert_tail(1)
    link_list.insert_index(7, 2)
    print(link_list.head)
    link_list.reverse()
    print(link_list.head)


if __name__ == "__main__":
    main()
