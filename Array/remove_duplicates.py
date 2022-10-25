""" 
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        slow, fast = 0, 0
        while fast < length:
            if nums[slow] != nums[fast]:
                nums[slow+1] = nums[fast]
                slow += 1
            fast += 1

        return slow + 1





if __name__ == "__main__":
    inputs = [1]
    inputs1 = [1, 1, 2]
    inputs2 = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    result = solution.removeDuplicates(inputs)
    print(f"Result: {result}")
    print(inputs[:result])
