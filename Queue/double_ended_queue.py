from typing import Optional


class DoubleLinkedNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[DoubleLinkedNode] = None
        self.pre: Optional[DoubleLinkedNode] = None


class DoubleEndedQueue:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.size = 0
        self.head: Optional[DoubleLinkedNode] = None
        self.tail: Optional[DoubleLinkedNode] = None

    def append(self, val: int) -> None:
        tail = DoubleLinkedNode(value=val)
        if self.size == 0:
            self.head = tail
            self.tail = tail
            self.size += 1
            return

        if self.size == self.max_size:
            self.popleft()

        self.tail.next = tail
        tail.pre = self.tail
        self.tail = tail
        self.size += 1

    def appendleft(self, val: int) -> None:
        head = DoubleLinkedNode(value=val)
        if self.size == 0:
            self.head = head
            self.tail = head
            self.size += 1
            return

        if self.size == self.max_size:
            self.pop()

        head.next = self.head
        self.head.pre = head
        self.head = head
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            raise IndexError("Empty queue")

        tail = self.tail
        self.tail = tail.pre
        self.size -= 1
        return tail.value

    def popleft(self) -> int:
        if self.size == 0:
            raise IndexError("Empty queue")

        head = self.head
        self.head = head.next
        self.size -= 1
        return head.value

    def __len__(self) -> int:
        return self.size


if __name__ == "__main__":
    dequeue = DoubleEndedQueue(max_size=3)

    dequeue.append(1)
    dequeue.append(2)
    dequeue.append(3)
    dequeue.append(4)

    print(dequeue.popleft())
    print(dequeue.popleft())
    print(dequeue.popleft())

    dequeue.appendleft(1)
    dequeue.appendleft(2)
    dequeue.appendleft(3)
    dequeue.appendleft(4)

    print(dequeue.popleft())
    print(dequeue.popleft())
    print(dequeue.popleft())

    print(len(dequeue))