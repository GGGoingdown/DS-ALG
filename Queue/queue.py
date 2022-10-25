from this import d
from typing import TypeVar, Generic, Optional

T  = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: int, next: T = None) -> None:
        self.value: int = value
        self.next = next


class Queue(Generic[T]):
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.length = 0
        self.front = None    
        self.end = None
    def peek(self) -> int:
        if self.length == 0:
            raise Exception("Empyt queue")
        return self.front.value

    def is_empty(self) -> bool:
        return True if self.length == 0 else False

    def enqueue(self, value: int) -> None:
        node: Node = Node(value)
        if self.length >= self.max_size:
            raise Exception("Max size limit")
        if self.length == 0:
            self.front = node
        else:
            self.end.next = node
        self.end = node
        self.length += 1

    def dequeue(self) -> int:
        if self.length == 0:
            raise Exception("Empyt queue")
        
        value = self.front.value
        self.front = self.front.next
        self.length -= 1
        return value


def main():
    queue = Queue(3)

    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue.length)




main()


