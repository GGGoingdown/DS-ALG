from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if (num-1) not in nums_set:
                length = 0
                while (num+length) in nums_set:
                    length += 1

                longest_seq = max(length, longest_seq)

        return longest_seq


if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # Consecutive is 1, 2, 3, 4, so return 4
    solution = Solution()
    result = solution.longestConsecutive(nums)

    print(result)
