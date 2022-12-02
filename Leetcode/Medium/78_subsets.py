from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp_nums = []
        idx = 0
        self._helper(nums, idx, result, tmp_nums)
        return result


    def _helper(self, nums: List[int], idx: int, result: List[List[int]], tmp_nums: List[int]) -> False:
        if idx >= len(nums):
            result.append(tmp_nums.copy())
            return False

        tmp_nums.append(nums[idx])
        self._helper(nums, idx+1, result, tmp_nums)
        tmp_nums.pop()
        self._helper(nums, idx+1, result, tmp_nums)

        

if __name__ == "__main__":
    solution = Solution()
    result = solution.subsets([1,2 ,3])

    print(result)


