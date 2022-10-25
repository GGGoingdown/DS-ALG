from re import L
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
        return slow + 1



def main():
    array = [1, 1, 2]
    solution = Solution()
    print(solution.removeDuplicates(array))



main()