from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r: int, c: int, i: int, cache: set) -> bool:

            if (
                min(r, c) < 0
                or r == len(board)
                or c == len(board[0])
                or (r, c) in cache
                or board[r][c] != word[i]
            ):
                return False

            if i == len(word) - 1:
                return True

            cache.add((r, c))
            result = (
                dfs(r + 1, c, i + 1, cache)
                or dfs(r - 1, c, i + 1, cache)
                or dfs(r, c + 1, i + 1, cache)
                or dfs(r, c - 1, i + 1, cache)
            )
            cache.remove((r, c))

            return result

        visit: set[tuple[int, int]] = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                result = dfs(i, j, 0, visit)
                if result:
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    solution = Solution()
    result = solution.exist(board, word="ABCE")
    print(result)
