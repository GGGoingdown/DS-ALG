from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ...


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)

    def check_value(k, v):
        print(k, v)
        return v

    v = Counter(nums)
    print(sorted(v, key=lambda x: v[x]))
