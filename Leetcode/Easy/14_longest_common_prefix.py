from typing import List 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_length = len(min(strs))

        for i in range(min_length):
            temp = ""
            for j in range(len(strs)):
                if j == 0:
                    temp = strs[j][i]
                else:
                    if strs[j][i] != temp:
                        temp = ""

            res += temp

        return res
            

def main():
    s = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(s))


main()
