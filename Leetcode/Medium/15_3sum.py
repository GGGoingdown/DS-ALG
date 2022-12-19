from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        nums.sort()

        for i, a in enumerate(nums):
            # avoid duplicate solution
            if i > 0 and a == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = a + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    result.append([a, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return result


def main():
    # nums = [-1,0,1,2,-1,-4]
    a = [0, 0, 0]
    solution = Solution()
    print(solution.threeSum(a))


main()
