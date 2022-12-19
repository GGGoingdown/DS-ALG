from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        L = 0
        for R in range(L, len(prices)):
            if prices[R] < prices[L]:
                L = R

            result = max(result, prices[R] - prices[L])

        return result


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices=prices)

    print(result)
