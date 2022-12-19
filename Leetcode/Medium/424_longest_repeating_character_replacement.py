class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count: dict[str, int] = {}

        L = 0
        maxf = 0

        for R in range(L, len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(maxf, count[s[R]])

            if (R - L + 1) - maxf > k:
                count[s[L]] = count[s[L]] - 1
                L += 1

            result = max(result, (R - L) + 1)

        return result


if __name__ == "__main__":
    s = "ABAB"
    # s = "AABABBA"
    k = 2
    solution = Solution()
    result = solution.characterReplacement(s, k)

    print(result)
