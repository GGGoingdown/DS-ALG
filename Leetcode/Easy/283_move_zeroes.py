from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """ 
    #         Time complexity: O(n*n)
    #         Space complexity: O(1)
    #     """
    #     n = len(nums)-1
    #     for i in range(n):
    #         j = i+1
    #         while j < len(nums):
    #             if nums[i] == 0 and nums[j] != 0:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #                 break
                    
    #             j += 1
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

def main():
    array = [0,1,0,3,12, 0]
    solution = Solution()
    solution.moveZeroes(array)
    print(array)

main()

