class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ...

    def _heapify(self):
        ...




if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    solution = Solution()
    result = solution.findKthLargest(nums=nums, k=2)

    print(result)
