""" 
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
1 <= n <= 1000
"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return [*nums, *nums]


if __name__ == "__main__":
    from utils import ResultValidator

    v1 = ResultValidator(inputs=[1], expected_result=[1, 1])
    v2 = ResultValidator(inputs=[1, 2, 3], expected_result=[1, 2, 3, 1, 2, 3])

    solution = Solution()
    for v in [v1, v2]:
        result = solution.getConcatenation(v.inputs)
        v.validate(result)
