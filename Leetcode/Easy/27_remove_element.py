from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        n = len(nums)-1
        pos = len(nums)-1
        for i in range(n, -1, -1):
            if nums[i] == val:
                nums[i], nums[pos] = nums[pos], nums[i]
                counter += 1
                pos -= 1

        return len(nums) - counter 


def main():
    array = [3]
    solution = Solution()
    print(solution.removeElement(array, 2))
    print(array)

main()
            