""" 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
---
Example :

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""


class Node:
    def __init__(self, val: int, min_val: int) -> None:
        self.val = val
        self.min_val = min_val


class MinStack:
    def __init__(self):
        self._stack: list[Node] = []
        self._minimal_val: int = float("inf")

    def push(self, val: int) -> None:
        # push(int val) pushes the element val onto the stack.
        min_val = min(self._minimal_val, val)
        self._minimal_val = min_val
        node = Node(val=val, min_val=min_val)
        self._stack.append(node)

    def pop(self) -> None:
        # pop() removes the element on the top of the stack.
        self._stack.pop()

    def top(self) -> int:
        #  top() gets the top element of the stack.
        node = self._get_last_node()
        return node.val

    def getMin(self) -> int:
        # getMin() retrieves the minimum element in the stack.
        node = self._get_last_node()
        return node.min_val

    def _get_last_node(self) -> Node:
        if len(self._stack) == 0:
            raise IndexError("Empty stack")
        node = self._stack[-1]
        return node


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
