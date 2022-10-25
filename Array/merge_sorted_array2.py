""" 
Example1: 
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example2 :
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example3 :
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
"""
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_index = m-1
    nums2_index = n-1

    last_index = (m + n) - 1

    if m == 0:
        nums1[:n] = nums2[:n]

    while nums1_index >= 0 or nums2_index >= 0:
        if nums2_index < 0:
            break

        if nums2[nums2_index] >= nums1[nums1_index]:
            nums1[last_index] = nums2[nums2_index]
            nums2_index -= 1

        else:
            nums1[last_index] = nums1[nums1_index]
            nums1[nums1_index] = 0
            nums1_index -= 1

        last_index -= 1


def main():
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)

    print(nums1)


if __name__ == "__main__":
    main()