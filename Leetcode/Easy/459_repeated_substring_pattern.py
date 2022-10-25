class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        for i in range(len(s) // 2):
            sub += s[i]
            x = len(s) // len(sub)
            if sub * x == s:
                return True

        return False

def main():
    st = "abcabcabcabc"
    solution = Solution()
    print(solution.repeatedSubstringPattern(st))



main()