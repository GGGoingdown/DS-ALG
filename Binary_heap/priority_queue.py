from math import ceil
from re import S
from typing import List, Optional


def left_child(i: int) -> int:
    return 2 * i + 1


def right_child(i: int) -> int:
    return 2 * i + 2


def parent(i: int) -> Optional[int]:
    if i == 0:
        return None
    return ceil((i - 2) / 2)


class MaxHeap:
    def __init__(self) -> None:
        self.array: List[int] = []
        self.length: int = 0

    def is_leaf(self, index) -> bool:
        if left_child(index) >= self.length and right_child(index) >= self.length:
            return True
        return False

    def fix_up(self):
        index = self.length - 1
        while (
            parent(index) is not None and self.array[parent(index)] < self.array[index]
        ):
            self.array[parent(index)], self.array[index] = (
                self.array[index],
                self.array[parent(index)],
            )
            index = parent(index)

    def fix_down(self):
        index = 0
        while not self.is_leaf(index):
            j = left_child(index)
            if j != len(self.array) - 1 and self.array[j] < self.array[j + 1]:
                j += 1
            if self.array[index] > self.array[j]:
                break

            self.array[j], self.array[index] = self.array[index], self.array[j]
            index = j

    def insert(self, num: int) -> None:
        self.array.append(num)
        self.length += 1
        self.fix_up()  # * To the right position

    def delete_max(self) -> int:
        if self.length == 0:
            raise Exception("Empty array")
        self.array[0], self.array[self.length - 1] = (
            self.array[self.length - 1],
            self.array[0],
        )
        value = self.array[self.length - 1]
        self.length -= 1
        self.array = self.array[: self.length]
        self.fix_down()
        return value


class MinHeap:
    def __init__(self) -> None:
        self.array: list[int] = []
        self.length: int = 0

    def _is_leaf(self, index: int) -> bool:
        li = left_child(index)
        ri = right_child(index)
        if li >= self.length and ri >= self.length:
            return True
        return False

    def fix_up(self, index: int) -> None:
        current_index = index
        parent_index = parent(current_index)
        while (
            parent_index is not None
            and self.array[current_index] < self.array[parent_index]
        ):
            self.array[current_index], self.array[parent_index] = (
                self.array[parent_index],
                self.array[current_index],
            )
            current_index = parent_index
            parent_index = parent(current_index)

    def fix_down(self, index: int) -> None:
        current_index = index
        while not self._is_leaf(current_index):
            j = left_child(current_index)
            if j != self.length - 1 and self.array[j] > self.array[j + 1]:
                j += 1

            if self.array[j] > self.array[current_index]:
                break

            self.array[current_index], self.array[j] = (
                self.array[j],
                self.array[current_index],
            )
            current_index = j

    def insert(self, value: int) -> None:
        self.array.append(value)
        if self.length > 0:
            self.fix_up(self.length)

        self.length += 1

    def delete(self) -> int:
        if self.length == 0:
            raise IndexError("Empty heap")

        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        value = self.array[-1]
        self.array = self.array[:-1]
        self.length -= 1
        self.fix_down(0)
        return value


def main():
    max_heap = MaxHeap()
    min_heap = MinHeap()
    from random import randint

    for _ in range(10):
        num = randint(1, 1000)
        max_heap.insert(num)
        min_heap.insert(num)

    max_li = []
    min_li = []
    for _ in range(10):
        max_li.append(max_heap.delete_max())
        min_li.append(min_heap.delete())

    print(max_li == min_li[::-1])


if __name__ == "__main__":
    # main()
    import heapq

    a = list(map(lambda x: x * -1, [5, 1, 0, 8, 7]))
    heapq.heapify(a)
    print(a)
    for _ in range(3):
        print(abs(heapq.heappop(a)))
        print(a)

    heapq.merge()