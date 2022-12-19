class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count: set = set()
        L = 0
        result = ""
        for R in range(L, len(s)):
            if s[R] in t:
                if len(count) == len(t):
                    while s[R] in count:
                        if s[L] in t:
                            count.remove(s[L])
                        L += 1

                    while s[L] not in t:
                        L += 1
                        
                count.add(s[R])

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    solution = Solution()
    result = solution.minWindow(s, t)
    print(result)
