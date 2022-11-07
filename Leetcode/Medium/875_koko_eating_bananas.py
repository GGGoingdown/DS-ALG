from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = []
        while low <= high:
            mid = (low + high) // 2
            total_hour = self._count_speed(piles, mid)
            print(f"High: {high} - Low: {low} - Mid: {mid} - Total hour: {total_hour}")
            if total_hour > h:
                low = mid + 1
            elif total_hour <= h:
                high = mid - 1
                res.append(mid)

        return min(res)

    def _count_speed(self, piles: List[int], speed: int) -> int:
        counter = 0
        for pile in piles:
            res = math.ceil(pile / speed)
            counter += res

        return counter


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    solution = Solution()
    result = solution.minEatingSpeed(piles=piles, h=h)
    print(result)
