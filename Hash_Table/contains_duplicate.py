from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        contains_dict: dict[int, int] = {}
        for num in nums:
            exist = contains_dict.get(num)
            if exist:
                return True

            contains_dict[num] = 1

        return False


if __name__ == "__main__":
    nums: list[int] = [1, 1, 2, 3]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)
