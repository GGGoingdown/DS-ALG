from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # TODO: Sorted
        nums.sort()
        total = 0
        min_diff = None

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s < target:
                    l += 1
                else:
                    r -= 1

                current_diff = abs(target - s)
                if min_diff is None:
                    min_diff = current_diff
                    total = s
                else:
                    if current_diff < min_diff:
                        total = s
                        min_diff = current_diff

        return total


def main():
    array = [-111, -111, 3, 6, 7, 16, 17, 18, 19]
    solution = Solution()
    print(solution.threeSumClosest(array, 13))


main()
