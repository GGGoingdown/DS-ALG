class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) == 0:
            return ""

        countT: dict[str, int] = {}
        window: dict[str, int] = {}

        for char_t in t:
            countT[char_t] = 1 + countT.get(char_t, 0)

        res = [-1, -1]
        minLen = float("infinity")
        L = 0
        have, need = 0, len(countT)

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (R - L + 1) < minLen:
                    minLen = R - L + 1
                    res[0], res[1] = L, R

                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1

                L += 1

        return s[res[0] : res[1] + 1] if minLen < float("infinity") else ""


if __name__ == "__main__":
    # s, t = "ADOBECODEBANC", "ABC"
    s, t = "a", "aa"

    solution = Solution()
    result = solution.minWindow(s, t)
    print(result)
