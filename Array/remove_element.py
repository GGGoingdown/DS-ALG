"""
LeetCode: https://leetcode.com/problems/remove-element/
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        length = len(nums)
        slow, fast = length - 1, length - 1
        while fast >= 0:
            if nums[fast] == val:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow -= 1

            fast -= 1

        return slow + 1


if __name__ == "__main__":
    from utils import ResultValidator

    v1 = ResultValidator(inputs=([], 2), expected_result=0)
    v2 = ResultValidator(inputs=([0, 1, 2, 2, 3, 0, 4, 2], 2), expected_result=5)
    v3 = ResultValidator(inputs=([0], 2), expected_result=1)

    solution = Solution()
    for v in [v1, v2, v3]:
        inputs, val = v.inputs
        result = solution.removeElement(inputs, val)
        v.validate(result)
