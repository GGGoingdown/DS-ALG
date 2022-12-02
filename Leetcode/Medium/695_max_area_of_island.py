from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int, visit: set) -> bool:
            if (
                min(r, c) < 0
                or r == len(grid)
                or c == len(grid[0])
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return False

            visit.add((r, c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

            return True

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = set()
                dfs(i, j, area)
                max_area = max(len(area), max_area)

        return max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    solution = Solution()
    result = solution.maxAreaOfIsland(grid=grid)
    print(result)
