from abc import abstractmethod


class Heap:
    def __init__(self) -> None:
        self._node: list[int] = [0]
        self._length: int = 0

    def get_leftNode(self, idx: int) -> int:
        return 2 * idx

    def get_rightNode(self, idx: int) -> int:
        return self.get_leftNode(idx) + 1

    def get_parent(self, idx: int) -> int:
        return idx // 2

    def show(self) -> None:
        print(self._node)

    @abstractmethod
    def fix_up(self, idx: int):
        pass

    @abstractmethod
    def fix_down(self, idx: int):
        pass


class MinHeap(Heap):
    def __init__(self) -> None:
        super().__init__()

    def fix_up(self, idx: int) -> None:
        cur_idx = idx
        while self.get_parent(cur_idx) > 0 and self.get_parent(cur_idx) <= self._length:
            if self._node[cur_idx] < self._node[self.get_parent(cur_idx)]:
                # If current node small than parent, swap
                self._node[cur_idx], self._node[self.get_parent(cur_idx)] = (
                    self._node[self.get_parent(cur_idx)],
                    self._node[cur_idx],
                )
                cur_idx = self.get_parent(cur_idx)
            else:
                break
                
    def fix_down(self, idx: int) -> None:
        cur_idx = idx
        while cur_idx <= self._length:
            j = self.get_leftNode(cur_idx)
            if j > self._length:
                break
            if j != self._length and self._node[j] > self._node[j+1]:
                j += 1

            if self._node[cur_idx] > self._node[j]:
                self._node[cur_idx], self._node[j] = self._node[j], self._node[cur_idx]
                cur_idx = j
            else:
                break

    def push(self, val: int) -> None:
        self._node.append(val)
        self._length += 1
        self.fix_up(self._length)

    def pop(self) -> int:
        if self._length <= 0:
            raise ValueError("Empty heap")
        
        if self._length == 1:
            val = self._node.pop()
            self._length -= 1
            return val

        self._node[self._length], self._node[1] = self._node[1], self._node[self._length]
        val = self._node.pop()
        self._length -= 1
        self.fix_down(1)
        return val



if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.push(18)
    min_heap.push(15)
    min_heap.push(12)
    min_heap.push(10)
    min_heap.push(9)
    # min_heap.show()
    for _ in range(3):
        print(min_heap.pop())
    min_heap.show()



