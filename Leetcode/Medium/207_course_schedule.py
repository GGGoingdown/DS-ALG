from typing import List


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         preMap: dict[int, list[int]] = {i: [] for i in range(numCourses)}
#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)

#         visitCrs: set = set()

#         def dfs(crs: int) -> bool:
#             if crs in visitCrs:
#                 return False

#             if len(preMap[crs]) == 0:
#                 return True

#             visitCrs.add(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False

#             visitCrs.remove(crs)
#             preMap[crs] = []
#             return True

#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False

#         return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap: dict[int, list[int]] = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitCrs: set = set()

        def dfs(crs: int) -> bool:
            if crs in visitCrs:
                return False

            if len(preMap[crs]) == 0:
                return True

            visitCrs.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitCrs.remove(crs)
            preMap[crs] = []
            return True

        for crs in preMap.keys():
            if not dfs(crs):
                return False

        return True


if __name__ == "__main__":
    numCourses = 5
    prerequisites = [[0, 1], [0, 2], [1, 3], [3, 4], [1, 4]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)

    # for i, a in prerequisites:
    #     print(i, a)
