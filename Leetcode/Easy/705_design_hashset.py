from typing import Optional


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.pre: Optional[Node] = None
        self.next: Optional[Node] = None


class MyHashSet:
    def __init__(self):
        self.size = 7
        self._hash_table: list[Node] = []

        for _ in range(self.size):
            head = Node(key=-1)
            self._hash_table.append(head)

    def add(self, key: int) -> None:
        idx = self._hash(key)
        cur_node = self._hash_table[idx]
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.key == key:
                return

        new_node = Node(key=key)
        cur_node.next = new_node
        new_node.pre = cur_node

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        cur_node = self._hash_table[idx].next
        while cur_node is not None:
            if cur_node.key == key:
                self._move_node(cur_node)
                break
            cur_node = cur_node.next

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        cur_node = self._hash_table[idx].next
        while cur_node is not None:
            if cur_node.key == key:
                return True
            cur_node = cur_node.next

        return False

    def _move_node(self, node: Node) -> None:
        node.pre.next = node.next
        if node.next is not None:
            node.next.pre = node.pre

    def _hash(self, key: int) -> int:
        return key % self.size


if __name__ == "__main__":
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(3)
    hashset.add(3)
    print(hashset.contains(3))

    print(hashset.contains(4))
    hashset.remove(4)
    hashset.remove(3)
    print(hashset.contains(3))