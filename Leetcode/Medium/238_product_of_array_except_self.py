import math
from typing import List
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_counter: dict[int, int] = defaultdict(int)
        for num in nums:
            num_counter[num] += 1

        zero_counter = num_counter.get(0)
        if zero_counter is not None and zero_counter >= 2:
            return [0] * len(nums)

        temp_sum = 1
        for num, counter in num_counter.items():
            if num == 0:
                continue

            temp_sum *= int(math.pow(num, counter))

        result: list[int] = []
        for num in nums:
            if zero_counter is not None:
                if num == 0:
                    result.append(temp_sum)
                else:
                    result.append(0)

                continue

            result.append(temp_sum // num)

        return result


if __name__ == "__main__":
    nums = [-1, 1, 0, -3, 3]
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)
