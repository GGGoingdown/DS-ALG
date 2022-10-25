class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def spread(s: str, l: int, r: int) -> int:
            counter = 0
            while l>=0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    counter += 2
                else:
                    temp_r = r 
                    while s[l] != s[temp_r]:
                        temp_r += 1



def main():
    s = ""
    solution = Solution()
    print(solution.longestPalindromeSubseq(s))


main()
