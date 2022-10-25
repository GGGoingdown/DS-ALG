class DoubleLinkedNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.previous = None



class DoubleEndedQueue:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

    def enqueue(self)