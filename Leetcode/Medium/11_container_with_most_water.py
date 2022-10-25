from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        length = len(height)
        for i in range(length-1):
            for j in range(i+1, length):
                current_area = min(height[i], height[j]) * (j-i) 
                area = max(current_area, area)

        return area

    # def maxArea(self, height: List[int]) -> int:
    #     length = len(height)
    #     l = 0
    #     r = length-1
    #     print(r)
    #     area = 0
        
    #     while l < r:
    #         current_area = min(height[l], height[r]) * (r-l)
    #         area = max(current_area, area)
            
    #         if height[l] < height[r]:
    #             l += 1
    #         else:
    #             r -= 1
                
    #     return area


def main():
    containers = [1,8,6,2,5,4,8,3,7]

    solution = Solution()
    print(solution.maxArea(containers))


main()