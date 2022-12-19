""" Question : How shortest path can reach from left-top to righ-down
 - - - - - - - - -
 | 0 | 0 | 0 | 0 |
 - - - - - - - - -
 | 1 | 1 | 0 | 0 |
 - - - - - - - - -
 | 0 | 0 | 0 | 1 |
 - - - - - - - - -
 | 0 | 1 | 0 | 0 |
 - - - - - - - - - 
"""
from collections import deque


def bfs(grid: list[list[int]]) -> int:
    queue = deque()
    visit = set()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while True:
        if len(queue) <= 0:
            return length

        for _ in range(len(queue)):
            r, c = queue.popleft()

            if r == len(grid) - 1 and c == len(grid) - 1:
                return length

            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
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
    grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    result = bfs(grid)
    print(result)