from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ...


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)
