class Solution:
    def longestPalindrome(self, s: str) -> str:
        def spread(s: str, l: int, r: int) -> str:
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""

        for i in range(len(s)):
            odd_len = spread(s, i, i)
            even_len = spread(s, i, i+1)
            res = max(odd_len, even_len, res, key=len)

        return res




def main():
    s = "aacabdkacaa"
    # s = "a"
    solution = Solution()
    print(solution.longestPalindrome(s))

main()