from typing import Optional

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        target_row_indx: Optional[int]= None
        while row_l <= row_r:
            row_mid = (row_l + row_r) // 2
            if target > matrix[row_mid][-1]:
                row_l = row_mid + 1
            elif target < matrix[row_mid][0]:
                row_r = row_mid - 1
            else:
                target_row_indx = row_mid
                break
                
        if target_row_indx is None:
            target_row_indx = row_l - 1


        target_list = matrix[target_row_indx]
        l, r = 0, len(target_list) - 1
        while l <= r:
            mid = (r+l)//2
            if target > target_list[mid]:
                l = mid + 1
            elif target < target_list[mid]:
                r = mid - 1
            else:
                return True

        return False



if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    solution = Solution()
    result = solution.searchMatrix(matrix=matrix, target=target)    
    print(result)