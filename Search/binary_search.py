class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (r + l)//2
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1



if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    result = solution.search(nums, target=target)
    print(result)
