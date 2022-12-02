""" 
Prefix tree

"""
from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.isWord: bool = False


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.node
        for w in word:
            if w not in cur_node.children:
                cur_node.children[w] = TrieNode()
            cur_node = cur_node.children[w]
        cur_node.isWord = True
        return

    def search(self, word: str) -> bool:
        cur_node = self.node
        for w in word:
            if w not in cur_node.children:
                return False
            cur_node = cur_node.children[w]

        if cur_node.isWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.node
        for w in prefix:
            if w not in cur_node.children:
                return False

            cur_node = cur_node.children[w]

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("add")
    trie.insert("rental")
    trie.insert("jam")
    # print(trie.search("hell"))
    # print(trie.search("helloa"))
    # print(trie.search("hello"))
    # print(trie.startsWith("hell"))
    print(trie.startsWith("ad"))
    # print(trie.startsWith("hello"))
