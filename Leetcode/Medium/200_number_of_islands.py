from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int, visit: set) -> bool:
            len_r, len_c = len(grid), len(grid[0])
            if (
                min(r, c) < 0
                or r == len_r
                or c == len_c
                or (r, c) in visit
                or grid[r][c] == "0"
            ):
                return False

            visit.add((r, c))

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

            return True

        count = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j, visit):
                    count += 1


        return count



if __name__ == "__main__":
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]

    solution = Solution()
    result = solution.numIslands(grid=grid)
    print(result)