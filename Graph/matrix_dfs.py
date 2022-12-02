""" Question : How many path can reach from left-top to righ-down
 - - - - - - - - -
 | 0 | 0 | 0 | 0 |
 - - - - - - - - -
 | 1 | 1 | 0 | 0 |
 - - - - - - - - -
 | 0 | 0 | 0 | 1 |
 - - - - - - - - -
 | 0 | 1 | 0 | 0 |
"""


def dfs(graph: list[list[int]], r: int, c: int, visit: set) -> int:
    len_r, len_c = len(graph), len(graph[0])

    if min(r, c) < 0 or r == len_r or c == len_c or (r, c) in visit or graph[r][c] == 1:
        return 0

    if r == len_r - 1 and c == len_c - 1:
        return 1

    visit.add((r, c))
    count = 0
    count += dfs(graph, r + 1, c, visit)
    count += dfs(graph, r - 1, c, visit)
    count += dfs(graph, r, c + 1, visit)
    count += dfs(graph, r, c - 1, visit)
    visit.remove((r, c))

    return count


if __name__ == "__main__":
    graph = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

    r, c = 0, 0
    visit = set()
    result = dfs(graph=graph, r=r, c=c, visit=visit)
    print(result)
