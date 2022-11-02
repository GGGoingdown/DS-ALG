def insertion_sort(nums: list[int]) -> None:
    def fix_down(nums: list[int], index: int) -> None:
        for j in range(index, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                continue
            break

    length = len(nums)
    if length <= 1:
        return

    for i in range(length - 1):
        if nums[i + 1] < nums[i]:
            fix_down(nums, i + 1)


def quick_sort(nums: list[int]) -> None:
    if len(nums) <= 1:
        return None
    #
    def helper(nums: list[int], first_idx: int, last_idx: int) -> None:
        if first_idx >= last_idx:
            return

        pivot = nums[first_idx]
        pos = last_idx

        for j in range(last_idx, first_idx, -1):
            if nums[j] > pivot:
                nums[j], nums[pos] = nums[pos], nums[j]
                pos -= 1

        nums[first_idx], nums[pos] = nums[pos], nums[first_idx]
        helper(
            nums, first_idx=pos + 1, last_idx=last_idx
        )  # Right side. Example -> [10, 8]
        helper(nums, first_idx=first_idx, last_idx=pos - 1)  # Left side. Example -> [5]

    first_idx = 0
    last_idx = len(nums) - 1
    helper(nums=nums, first_idx=first_idx, last_idx=last_idx)


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) > 1:
        mid = len(nums) // 2
        left_array = nums[:mid]
        right_array = nums[mid:]
        merge_sort(left_array)
        merge_sort(right_array)

        head_l, head_r, index = 0, 0, 0

        while head_l < len(left_array) and head_r < len(right_array):
            if left_array[head_l] < right_array[head_r]:
                nums[index] = left_array[head_l]
                head_l += 1
            else:
                nums[index] = right_array[head_r]
                head_r += 1

            index += 1

        while head_l < len(left_array):
            nums[index] = left_array[head_l]
            head_l += 1
            index += 1

        while head_r < len(right_array):
            nums[index] = right_array[head_r]
            head_r += 1
            index += 1

        return nums
    else:
        return nums


if __name__ == "__main__":
    a = [7, 1, 10, 9, 8]
    merge_sort(a)
    print(a)
