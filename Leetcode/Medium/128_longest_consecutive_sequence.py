from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lookup_table: dict[int, bool] = {}
        for num in nums:
            lookup_table[num] = True

        global_longest_con = 0
        for num in lookup_table:
            loc_longest_con = 0
            for i in range(1, len(nums)):
                v = lookup_table.get(num + i)
                if v is None:
                    break
                loc_longest_con += 1

            global_longest_con = max(loc_longest_con, global_longest_con)

        return global_longest_con + 1


if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]  # Consecutive is 1, 2, 3, 4, so return 4
    solution = Solution()
    result = solution.longestConsecutive(nums)

    print(result)
