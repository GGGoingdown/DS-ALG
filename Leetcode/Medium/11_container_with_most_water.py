from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """  由於水面只能是平的 所以兩側只保留最高點
        area = width * height  
        """
        maxContain = 0
        L, R = 0, len(height) - 1
        while L < R:
            width = R - L
            if height[L] < height[R]:
                curContain = width * height[L]
                L += 1
            else:
                curContain = width * height[R]
                R -= 1

            maxContain = max(curContain, maxContain)

        return maxContain


def main():
    containers = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    print(solution.maxArea(containers))


main()
