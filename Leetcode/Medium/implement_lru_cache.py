from collections import OrderedDict
from typing import Optional


class LRU:
    def __init__(self, max_size: int) -> None:
        self._table = OrderedDict()
        self._cur_size = 0
        self._max_size = max_size

    def get(self, key: str) -> int:
        if key not in self._table:
            raise KeyError(key)
        self._table.move_to_end(key, last=True)
        return self._table[key]

    def insert(self, key: str, value: int) -> None:
        if key in self._table:
            self._table.move_to_end(key, last=True)
            self._table[key] = value
            return

        if self._cur_size >= self._max_size:
            self._table.popitem(last=False)

        self._table[key] = value
        self._cur_size += 1

    def show(self) -> None:
        for key, val in self._table.items():
            print(f"{key} - {val}")
        print("")


class LRUCache:
    def __init__(self, capacity: int):
        self._max_isze = capacity
        self._table = OrderedDict()
        self._cur_size = 0

    def get(self, key: int) -> int:
        if key not in self._table:
            return -1

        self._table.move_to_end(key, last=True)
        return self._table[key]

    def put(self, key: int, value: int) -> None:
        if key in self._table:
            self._table.move_to_end(key)
            self._table[key] = value
            return

        if self._cur_size >= self._max_isze:
            self._table.popitem(last=False)

        self._table[key] = value
        self._cur_size += 1


class Node:
    def __init__(self, key: str, val: str) -> None:
        self.key = key
        self.val = val
        self.next: Optional[Node] = None
        self.pre: Optional[Node] = None


class LRUModel:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self._hash: dict[str, Node] = {}
        self.head = Node(key="#", val="#")
        self.tail = Node(key="#%", val="#%")
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: str) -> str:
        if key not in self._hash:
            raise KeyError(key)

        node = self._hash[key]
        self.remove_the_node(node)
        self.move_to_head(node)
        return node.val

    def insert(self, key: str, val: str) -> None:
        if key in self._hash:
            node = self._hash[key]
            self.remove_the_node(node)
            self.move_to_head(node)
            node.val = val
            return

        if self.size >= self.capacity:
            self.pop()

        node = Node(key=key, val=val)
        self._hash[key] = node
        self.move_to_head(node=node)
        self.size += 1

    def remove_the_node(self, node: Node) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre

    def move_to_head(self, node: Node) -> None:
        node.pre = self.head
        node.next = self.head.next

        self.head.next.pre = node
        self.head.next = node

    def pop(self) -> None:
        last_node = self.tail.pre
        del self._hash[last_node.key]
        self.tail.pre = last_node.pre
        last_node.pre.next = self.tail
        self.size -= 1

    def show_link(self) -> None:
        cur_node = self.head
        while cur_node:
            print(f"{cur_node.key} - {cur_node.val}")
            cur_node = cur_node.next


if __name__ == "__main__":
    lru = LRUModel(capacity=3)
    lru.insert("eddie", "hello1")
    lru.insert("peter", "hello2")
    lru.insert("alice", "hello3")
    lru.insert("foo", "hello4")
    lru.insert("peter", "hello1")
    lru.show_link()
    lru.get("alice")
    lru.show_link()
    lru.insert("simon", "hello1")
    lru.show_link()
