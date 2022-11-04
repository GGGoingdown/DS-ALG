from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: list[int] = []
        lookup_table: dict[int, int] = {}  # key=number, valule=index

        for idx, num in enumerate(nums):
            lookup_num = target - num
            lookup_idx = lookup_table.get(lookup_num)
            if lookup_idx is not None:
                return [idx, lookup_idx]

            lookup_table[num] = idx

        return result


if __name__ == "__main__":
    nums = [9, 7, 11, 2]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums=nums, target=target)
    print(result)
