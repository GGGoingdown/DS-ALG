""" 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    minus_table: dict[int, int] = {}
    for current_index, num in enumerate(nums):
        if (num1_index := minus_table.get(num)) is not None:
            return [num1_index, current_index]

        ex_num = target - num
        minus_table[ex_num] = current_index

def main():
    nums = [1, 5, 9]
    target = 10
    print(twoSum(nums, target))


main()