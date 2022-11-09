from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        min_val = nums[left]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] < min_val:
                min_val = nums[mid]

        return min_val


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    solution = Solution()
    result = solution.findMin(nums2)
    print(result)
