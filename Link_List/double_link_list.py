class DoubleLinkedNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _check_length(self):
        if self.length == 0:
            raise Exception("Empty list")

    def add_front(self, value: int) -> None:
        node = DoubleLinkedNode(value)
        if self.length == 0:
            self.tail = node
        else:
            current_head = self.head
            current_head.previous = node
            node.next = current_head
        self.head = node
        self.length += 1

    def add_back(self, value: int) -> None:
        node = DoubleLinkedNode(value)
        if self.length == 0:
            self.head = node
        else:
            current_tail = self.tail
            current_tail.next = node
            node.previous = current_tail
        self.tail = node
        self.length += 1

    def get_back(self) -> int:
        self._check_length()

        v = self.tail.value
        self.tail = self.tail.previous
        self.length -= 1
        return v

    def get_front(self) -> int:
        self._check_length()
        v = self.head.value
        self.head = self.head.next
        self.length -= 1
        return v


def main():
    double_link = DoubleLinkedList()

    double_link.add_front(10)
    double_link.add_back(20)
    double_link.add_front(30)

    print(double_link.get_front())
    print(double_link.get_front())
    print(double_link.get_front())


main()