from typing import List

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)
#         count = k
#         if length <= 1:
#             count = 0
#         while count:
#             for i in range(0, length-1): 
#                 if i == 0:
#                     current = nums[i]
#                 else:
#                     current = current_next
#                 current_next: int = nums[i+1]
#                 nums[i+1] = current

#             nums[0] = current_next
#             count -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k > len(nums):
            mod_k = k%l
            slice_k = -(mod_k)
        else:
            slice_k = -(k)
        rotate_nums = []

        rotate_nums.extend(nums[slice_k:])
        rotate_nums.extend(nums[:slice_k])
        print(rotate_nums)
        nums[:] = rotate_nums





def main():
    # Situation: K > Array length
    array = [1, 2]
    k = 3
    solution = Solution()
    solution.rotate(array, k=k)
    assert array == [2, 1], f"Get error - {array}"

    # Situation: K = 1, Array length = 1
    array = [1]
    k = 1
    solution = Solution()
    solution.rotate(array, k=k)
    assert array == [1], f"Get error - {array}"




main()