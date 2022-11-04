import random


# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         target_idx = k - 1

#         first_idx = 0
#         last_idx = len(nums) - 1

#         return self._quick_sort(
#             nums, first_idx=first_idx, last_idx=last_idx, target_index=target_idx
#         )

#     def _quick_sort(
#         self, nums: list[int], first_idx: int, last_idx: int, target_index: int
#     ) -> int:
#         pivot = nums[first_idx]
#         pos = last_idx

#         for i in range(last_idx, first_idx, -1):
#             if nums[i] < pivot:
#                 nums[i], nums[pos] = nums[pos], nums[i]
#                 pos -= 1

#         nums[first_idx], nums[pos] = nums[pos], nums[first_idx]

#         if target_index < pos:
#             return self._quick_sort(
#                 nums, first_idx=first_idx, last_idx=pos - 1, target_index=target_index
#             )
#         elif target_index > pos:
#             return self._quick_sort(
#                 nums, first_idx=pos + 1, last_idx=last_idx, target_index=target_index
#             )
#         else:
#             return nums[pos]


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = random.choice(nums)
        left = []
        right = []
        mid = []
        for num in nums:
            if num == pivot:
                mid.append(num)
                continue
            if num > pivot:
                left.append(num)
                continue
            if num < pivot:
                right.append(num)
                continue

        mid_len, left_len = len(mid), len(left)
        if k <= left_len:
            return self.findKthLargest(left, k)
        elif k > (left_len + mid_len):
            return self.findKthLargest(right, k - left_len - mid_len)
        else:
            return mid[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    result = solution.findKthLargest(nums=nums, k=k)
    print(result)
