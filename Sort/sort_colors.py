""" 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter_buckets: list[int] = [0, 0, 0] # red, white and blue
        for num in nums:
            counter_buckets[num] += 1
        
        i = 0
        for bucket in range(len(counter_buckets)):
            count = counter_buckets[bucket]
            for _ in range(count):
                nums[i] = bucket
                i += 1


if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)