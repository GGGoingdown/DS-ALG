class Solution:
    def findDuplicate(self, nums: list[str]) -> list[list[str]]:
        lastAppear: dict[str, int] = {}
        numsIndex: dict[str, int] = {}
        result: list[list[str]] = []
        curIndex: int = 0

        for i, s in enumerate(nums):
            if s in lastAppear and lastAppear[s] == i - 1:
                if s in numsIndex:
                    # Update old one
                    result[numsIndex[s]].append(s)
                else:
                    # Create new one
                    result.append([s] * 2)
                    numsIndex[s] = curIndex
                    curIndex += 1

            lastAppear[s] = i

        return result


if __name__ == "__main__":
    nums = ["a", "a", "b", "a", "c", "c", "c", "d", "c", "d", "f", "f", ""]
    solution = Solution()
    result = solution.findDuplicate(nums)

    print(result)
