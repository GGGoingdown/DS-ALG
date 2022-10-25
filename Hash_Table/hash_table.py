from typing import List, Any, Optional

class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.data: List = [-1]*self.size

    def _hash(self, key: str) -> int:
        char_sum = sum([ord(c) for c in key])
        address = char_sum % self.size
        print(f"Hashing - {address}")
        return address


    def set(self, key: str, value: Any) -> None:
        address = self._hash(key)
        if self.data[address] == -1:
            self.data[address] = []
        self.data[address].append([key, value])
        return None

    def get(self, key: str) -> Optional[int]:
        address = self._hash(key)
        if self.data[address] == -1:
            return None

        for idx in self.data[address]:
            if idx[0] == key:
                return idx[1]

        return None


def main():
    hash_table = HashTable(2)

    hash_table.set("hello", 2)
    hash_table.set("Hello", 3)

    print(hash_table.get("h"))
main()