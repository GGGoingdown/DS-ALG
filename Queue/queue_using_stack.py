class QueueUsingStack1:
    def __init__(self) -> None:
        self.s1: list[int] = []
        self.s2: list[int] = []

    def enqueue(self, value: int) -> None:
        self.s1.append(value)

    def dequeue(self) -> int:
        if len(self.s1) == 0:
            raise Exception("Empty queue")

        while len(self.s1):
            self.s2.append(self.s1.pop())

        value = self.s2.pop()

        while len(self.s2):
            self.s1.append(self.s2.pop())

        return value


    def peek(self) -> int:
        if len(self.s1) == 0:
            raise Exception("Empty queue")

        return self.s1[0]


def main():
    queue = QueueUsingStack1()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


main()