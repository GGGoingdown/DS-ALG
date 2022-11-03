class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target_idx = k - 1

        first_idx = 0
        last_idx = len(nums) - 1

        pos = self._quick_sort(nums, first_idx=first_idx, last_idx=last_idx)

        while True:
            if pos == target_idx:
                return nums[pos]
            if target_idx > pos:
                _first_idx = pos + 1
                if len(nums[_first_idx : (last_idx + 1)]) <= 2:
                    return nums[pos + 1]

                pos = self._quick_sort(nums, _first_idx, last_idx=last_idx)
            else:
                if len(nums[first_idx:pos]) <= 2:
                    return nums[pos - 1]

                pos = self._quick_sort(nums, first_idx, last_idx=pos - 1)

    def _quick_sort(self, nums: list[int], first_idx: int, last_idx: int) -> int:
        pivot = nums[first_idx]
        pos = last_idx

        for i in range(last_idx, first_idx, -1):
            if nums[i] < pivot:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos -= 1

        nums[first_idx], nums[pos] = nums[pos], nums[first_idx]
        return pos


if __name__ == "__main__":
    nums = [-1, 2, 0]
    k = 2
    solution = Solution()
    result = solution.findKthLargest(nums=nums, k=k)
    print(result)
