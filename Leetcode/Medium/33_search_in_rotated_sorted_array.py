from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left_idx, right_idx = 0, len(nums) - 1
        while nums[left_idx] > nums[right_idx] and left_idx < right_idx:
            left_idx += 1

        right_gp_result = self.bs(nums, left_idx, right_idx, target)
        if right_gp_result != -1:
            return right_gp_result

        left_gp_result = self.bs(nums, 0, left_idx - 1, target)
        return left_gp_result

    def bs(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    nums = [
        7,
        0,
        1,
        2,
        4,
        5,
        6,
    ]
    target = 4
    solution = Solution()
    result = solution.search(nums=nums, target=target)
    print(result)
