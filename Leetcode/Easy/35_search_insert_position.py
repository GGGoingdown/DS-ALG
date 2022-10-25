from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        
        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid 
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if target == nums[l] or target < nums[l]:
            return l 
        return l + 1



def main():
    array = [1]
    solution = Solution()
    print(solution.searchInsert(array, 1))


main()
            