class Node:
    def __init__(self, value: int, next = None) -> None:
        self.value = value
        self.next = next


class StackLinkList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None

    def push(self, value: int) -> None:
        new_node = Node(value=value)
        current_node = self.head
        self.head = new_node
        if current_node != None:
            self.head.next = current_node
        
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            raise IndexError("Empty stack")
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

class StackArray:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.length = len(self.stack)

    def peek(self) -> int:
        if self.length == 0:
            raise Exception("Empty stack")
        return self.stack[-1]
    
    def pop(self) -> int:
        if self.length == 0:
            raise Exception("Empty stack")
        value = self.stack.pop()
        self.length -= 1
        return value

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.length += 1


def main():
    stack = StackArray()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

main()

