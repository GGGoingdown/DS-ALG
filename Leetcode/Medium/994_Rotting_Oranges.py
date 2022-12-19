from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def bfs(rotte_grid: list[tuple[int, int]], visit: set):
            if len(rotte_grid) == 0:
                return 0

            queue = deque()
            for rotte in rotte_grid:
                queue.append(rotte)
                visit.add(rotte)

            minutes = 0
            while True:
                if len(queue) <= 0:
                    return minutes - 1

                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    print(r, c)

                    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for pos_r, pos_c in neighbors:
                        new_r, new_c = r + pos_r, c + pos_c

                        if (
                            min(new_r, new_c) < 0
                            or new_r == len(grid)
                            or new_c == len(grid[0])
                            or (new_r, new_c) in visit
                            or grid[new_r][new_c] != 1
                        ):
                            continue

                        queue.append((new_r, new_c))
                        visit.add((new_r, new_c))

                minutes += 1

        rotte_grid: list[tuple[int, int]] = []
        fresh_grid: set[tuple[int, int]] = set()
        visit: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                if value == 2:
                    rotte_grid.append((i, j))
                if value == 1:
                    fresh_grid.add((i, j))

        minutes = bfs(rotte_grid, visit)
        if len(fresh_grid.difference(visit)):
            print(fresh_grid.difference(visit))
            return -1
        return minutes


if __name__ == "__main__":
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

    solution = Solution()
    result = solution.orangesRotting(grid)
    print(result)
