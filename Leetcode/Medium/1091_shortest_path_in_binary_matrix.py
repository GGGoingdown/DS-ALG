from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1

        queue = deque()
        visit: set[tuple[int, int]] = set()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 1
        while True:
            if len(queue) <= 0:
                return -1

            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length

                neighbors = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                    (1, 1),
                    (1, -1),
                    (-1, 1),
                    (-1, -1),
                ]

                for r_pos, c_pos in neighbors:
                    new_r, new_c = r + r_pos, c + c_pos
                    if (
                        min(new_r, new_c) < 0
                        or new_r == len(grid)
                        or new_c == len(grid[0])
                        or (new_r, new_c) in visit
                        or grid[new_r][new_c] == 1
                    ):
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))

            length += 1



if __name__ == "__main__":
    grid1 = [[0, 1], [1, 0]]
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    solution = Solution()
    result = solution.shortestPathBinaryMatrix(grid=grid2)
    print(result)
