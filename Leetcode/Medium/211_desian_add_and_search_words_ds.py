class TrieNode:
    def __init__(
        self,
    ) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isWord: bool = False


class WordDictionary:
    def __init__(self):
        self.trie_node = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.trie_node
        for w in word:
            if w not in cur_node.children:
                cur_node.children[w] = TrieNode()

            cur_node = cur_node.children[w]

        cur_node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root: TrieNode):
            cur_node = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for children in cur_node.children.values():
                        if dfs(i + 1, children):
                            return True

                    return False

                else:
                    if c not in cur_node.children:
                        return False

                    cur_node = cur_node.children[c]

            return cur_node.isWord

        return dfs(0, self.trie_node)


if __name__ == "__main__":
    solution = WordDictionary()
    for word in ["bad", "dad", "mad"]:
        solution.addWord(word)

    print(solution.search("b.."))
